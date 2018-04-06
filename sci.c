//------------------------------------------------------------------------------
//              Copyright (c) awaptec GmbH
//------------------------------------------------------------------------------
//
// \file        sci.c
// \brief       serial communication interface driver
// \author      Christian Jost, christian.jost@awaptec.ch
// \date        27.10.2013
//
//------------------------------------------------------------------------------
// Repository:
//      $Id: sci.c 741 2017-12-02 07:39:55Z chj-hslu $
//------------------------------------------------------------------------------

#include "sci.h"
#include "IO_Map.h"

#define BAUDRATE        19200		// 8 DataBit, 1 Stopp, No Parity

#define NEW_LINE        '\n'

#define __DSB()                     __asm volatile("dsb")
#define __ISB()                     __asm volatile("isb")

#define AB_CONCAT2(s1, s2)          s1##s2
#define AB_CONCAT(s1, s2)           AB_CONCAT2(s1, s2)


// K64, UART0-Rx = PTA1 Alt2, UART0-Tx = PTA2 Alt2, UART0 verwendet System clock
#define UART                        UART0
#define SET_RX_PIN_TO_UART()        (PORTA_PCR1 = PORT_PCR_MUX(2) | PORT_PCR_PE_MASK | PORT_PCR_PS_MASK)       // configure MUX PTA1 => ALT 2 UART0_RX
#define SET_TX_PIN_TO_UART()        (PORTA_PCR2 = PORT_PCR_MUX(2) | PORT_PCR_PE_MASK | PORT_PCR_PS_MASK)       // configure MUX PTA2 => ALT 2 UART0_TX
#define BAUDCLOCK                   120000000                              // 120 MHz system clock for UART 0 & 1
#define SET_UART_CLOCK_GATING()     (SIM_SCGC4 |= SIM_SCGC4_UART0_MASK)   // configure clock gating for UARTx

__attribute__( ( always_inline ) ) static inline void ENABLE_SCI_INTERRUPTS(void) {
  NVICISER0 = (1 << 31);      // enable interrupt 31
  NVICISER1 = (1 << 0);       // enable interrupt 32
}

__attribute__( ( always_inline ) ) static inline void DISABLE_SCI_INTERRUPTS(void) {
  NVICICER0 = (1 << 31);      // disable interrupt 31
  NVICICER1 = (1 << 0);       // disable interrupt 32
  __DSB();                    // data synchronization barrier
  __ISB();                    // instruction synchronization barrier
}



#define UART_BDL                    AB_CONCAT(UART,_BDL)  // UARTx_BDL
#define UART_BDH                    AB_CONCAT(UART,_BDH)  // UARTx_BDH
#define UART_D                      AB_CONCAT(UART,_D)    // UART_D
#define UART_C1                     AB_CONCAT(UART,_C1)   // UARTx_C1
#define UART_C2                     AB_CONCAT(UART,_C2)   // UARTx_C2
#define UART_C3                     AB_CONCAT(UART,_C3)   // UARTx_C3
#define UART_C4                     AB_CONCAT(UART,_C4)   // UARTx_C4
#define UART_S1                     AB_CONCAT(UART,_S1)   // UARTx_S1
#define UART_S2                     AB_CONCAT(UART,_S2)   // UARTx_S2


// Sendequeue
static char txBuf[SCI_TX_BUF_SIZE];
static volatile uint8 txBufCount;       // ERROR
static uint8 txBufWritePos;
static uint8 txBufReadPos;

// Empfangsqueue
static char rxBuf[SCI_RX_BUF_SIZE];
static volatile uint8 rxBufCount;
static uint8 rxBufWritePos;
static uint8 rxBufReadPos;

#if ((SCI_RX_BUF_SIZE > 255) || (SCI_RX_BUF_SIZE < 1)) 
#error ACHTUNG: SCI_RX_BUF_SIZE muss zwischen 1..255 sein!
#endif

#if (SCI_TX_BUF_SIZE > 255 || (SCI_TX_BUF_SIZE < 1)) 
#error ACHTUNG: SCI_TX_BUF_SIZE muss zwischen 1..255 sein!
#endif       


void ISR_UART_SCI(void)
{
    uint8 status = UART_S1;
    
    if (status & UART_S1_RDRF_MASK)
    {
        char ch = UART_D;
        if (rxBufCount < SCI_RX_BUF_SIZE)
        {
          rxBuf[rxBufWritePos] = ch;      // empf. Zeichen in der Queue speichern
          rxBufCount++;
          rxBufWritePos++;
          if (rxBufWritePos == SCI_RX_BUF_SIZE) rxBufWritePos = 0;
        }
    }
    
    if (status & UART_S1_TDRE_MASK)
    {
        // read from the tx buffer and write the data into the sci data register.
        // Disable tx interrupt if tx buffer is empty
        if (txBufCount > 0)
        {
          UART_D = txBuf[txBufReadPos];
          txBufCount--;
          txBufReadPos++;
          if (txBufReadPos == SCI_TX_BUF_SIZE) txBufReadPos = 0;      
        }
        else
        {
          // Buffer leer => Transmit Data Register Empty Interrupt deaktivieren.
          // wird später durch sciWriteByte() wieder aktiviert...
          UART_C2 &= ~UART_C2_TIE_MASK;
        }   
    }
    
    if (status & (UART_S1_OR_MASK | UART_S1_NF_MASK | UART_S1_FE_MASK))
    {
        (void)UART_D;
    }
}


/**
 * Liest ein Zeichen von der seriellen Schnittstelle.
 *
 * @return
 *      Der Aufruf ist blockierend, d.h. falls der Empfangsbuffer leer ist wird 
 *      gewartet bis ein Zeichen empfangen wird.
 */
char sciReadChar(void)
{
    char ch;
    while(rxBufCount == 0);     // Warten bis min. 1 Zeichen verfügbar ist
    
    //uint8 rie = loadAndClear8(&UART1_C2, UART_C2_RIE_SHIFT); // Empfangsinterrupt sperren
    DISABLE_SCI_INTERRUPTS();   // Disable UART interrupts
      ch = rxBuf[rxBufReadPos];
      rxBufCount--;
      rxBufReadPos++;
      if (rxBufReadPos == SCI_RX_BUF_SIZE) rxBufReadPos = 0; 
    ENABLE_SCI_INTERRUPTS();    // Enable UART interrupts
    
    //if (rie) bitSet8(&UART1_C2, UART_C2_RIE_MASK);           // Empfangsinterrupt wiederherstellen
    
    return ch;
}


/**
 * Schreibt ein Byte in die Sendequeue
 *
 * @details
 *      durch das aktivieren des SendeInterrupts (TIE) wird sofort ein Interrupt ausgelöst,
 *      falls Platz im Sendepuffer des SCI-Moduls vorhanden ist.
 *
 * @param [in] ch
 *      das zu sendende Byte
 */
void sciWriteChar(char ch)
{
  
  while (txBufCount >= SCI_TX_BUF_SIZE);  // Warten bis Platz in der Sendequeue
  
  //uint8 tie = loadAndClear8(&UART1_C2, UART_C2_TIE_SHIFT); // Empfangsinterrupt sperren
  //bitClr8(&UART1_C2, UART_C2_TIE_MASK);     // Empfangsinterrupt sperren
  
  
  DISABLE_SCI_INTERRUPTS();   // Disable UART interrupts, kritischer Code
    txBuf[txBufWritePos] = ch;
    txBufCount++;
    txBufWritePos++;
    if (txBufWritePos == SCI_TX_BUF_SIZE) txBufWritePos = 0;
  ENABLE_SCI_INTERRUPTS();
  

  UART0_C2 |= UART_C2_TIE_MASK;
  //bitSet8(&UART_C2, UART_C2_TIE_MASK);      // Sendeinterrupt aktivieren falls nicht aktiviert.
}


/**
 * liest einen String von der seriellen Schnittstelle
 *
 * @details
 * Liest solange Zeichen von der seriellen Schnittstelle bis er mit einem LineFeed abgeschlossen
 * wird oder die maximale Länge erreicht wird. Das LineFeed-Zeichen wird durch das nullterminierungs
 * Zeichen ersetzt.
 *
 * @param [in] str
 *      ein Puffer, in der der String geschrieben werden kann
 * @param [in] length
 *      die Länge des Puffers
 *
 * @return
 *      die Anzahl gelesener Zeichen.
 */
uint16 sciReadLine(char *str, uint16 length)
{
  unsigned int i;
  for (i=1; i<length; i++)
  {
    *str = sciReadChar();
    if (*str == NEW_LINE)
    {
      *str = '\0';
      break;
    }
    str++;
  }
  return i;
}


/**
 * Gibt einen String auf der seriellen Schnittstelle aus.
 *
 * Der String muss nullterminiert sein!
 *
 * @param [in] str
 *      der nullterminierte String
 */
void sciWrite(const char *str)
{
  if (str == 0) return;
  while(*str != 0) sciWriteChar(*str++);
}


/**
 * Gibt einen String auf der seriellen Schnittstelle aus.
 *
 * Der String muss nullterminiert sein! Anschliessend wird noch ein Linefeed hinzugefügt.
 *
 * @param [in] str
 *      der nullterminierte String
 */
void sciWriteLine(const char *str)
{
  sciWrite(str);
  sciWriteChar(NEW_LINE);
}


/**
 * Prüft, ob eine Zeile empfangen wurde, d.h ein Newline im Buffer steht.
 * 
 * @return
 *      true, falls ein Newline-Zeichen vorhanden ist, ansonsten false (0)
 */
bool sciHasLineReceived(void)
{   
  uint16 i;   
  uint16 index = rxBufReadPos;

  for (i=0; i<rxBufCount; i++)
  {        
    if (rxBuf[index] == NEW_LINE) return 1;
    if (++index == SCI_RX_BUF_SIZE) index = 0;
  }
  
  return 0;
}


/**
 * returns the number of bytes in the receive buffer
 * 
 * @return
 *    the number of bytes in the receive buffer.
 */
uint8 sciGetRxCount(void)
{
  return rxBufCount;
}


/**
 * Clears the receive buffer.
 */
void sciDiscardRxBuffer(void)
{
    //uint8 rie = loadAndClear8(&UART1_C2, UART_C2_RIE_SHIFT); // Empfangsinterrupt sperren
  
  DISABLE_SCI_INTERRUPTS();
  rxBufCount = 0;          // RX-Buffer initialisieren
  rxBufWritePos = 0;
  rxBufReadPos = 0;
  ENABLE_SCI_INTERRUPTS();
  //  if (rie) bitSet8(&UART1_C2, UART_C2_RIE_MASK);           // Empfangsinterrupt wiederherstellen       
}



void sciInit(void)
{   
    txBufReadPos = txBufWritePos = txBufCount = 0;
    rxBufReadPos = rxBufWritePos = rxBufCount = 0;
    
    // configure UARTx
    SET_RX_PIN_TO_UART();
    SET_TX_PIN_TO_UART();

    SET_UART_CLOCK_GATING();                    // configure clock gating for UARTx (Baud Clock = Busclock)        

    uint32 bd = ((BAUDCLOCK * 10) / (16 * BAUDRATE) + 5) / 10; // configure baudrate
    UART_BDH |= (bd >> 8) & 0xFF;
    UART_BDL |= (uint8)(bd & 0xFF);

    UART_C2 |= UART_C2_RIE_MASK;               // Receiver Interrupt Enable for RDRF
    UART_C2 |= UART_C2_RE_MASK;                // Receiver enable
    UART_C2 |= UART_C2_TE_MASK;                // Transmitter enable
    UART_C3 |= (UART_C3_ORIE_MASK | UART_C3_NEIE_MASK | UART_C3_FEIE_MASK);
    

//    
//    NVIC_IPR3 = (NVIC_IPR3 & ~NVIC_IP_PRI_13(0xFF)) | NVIC_IP_PRI_13(2<<6);     // set interrupt priority high=0, low=3
//    NVIC_ICPR |= (1 << 13);                     // clear pending interrupt 13
//    NVIC_ISER |= (1 << 13);                     // enable interrupt 13
//    
    
}

import serial

"""
Base implementation of the serial communication

Initialisation example:
>> frdm = SerialCommunicator.getInstance()
"""
class SerialCommunicator:
    # Here will be the instance stored.
    __instance = None
    __port = None
    __ENCODING = 'utf-8'

    # Settings for the serial port
    __PORT = '/dev/serial0'
    __BAUDRATE = 19200
    __BYTESIZE = serial.EIGHTBITS
    __PARITY = serial.PARITY_NONE
    __STOPBITS = serial.STOPBITS_ONE
    __TIMEOUT = 0

    @staticmethod
    def getInstance():
        # Static access method.
        if SerialCommunicator.__instance == None:
            SerialCommunicator()
        return SerialCommunicator.__instance

    # This constructor would be private if he could.
    def __init__(self):
        if SerialCommunicator.__instance != None:
            raise Exception('This class is a singleton!')
        else:
            SerialCommunicator.__instance = self
            self.__port = serial.Serial(port=self.__PORT, baudrate=self.__BAUDRATE, bytesize=self.__BYTESIZE, parity=self.__PARITY, stopbits=self.__STOPBITS)

    def receive(self):
        answer = lasttwo = ''
        while True:
            nextchar = self.__port.read()
            answer += nextchar
            lasttwo = lasttwo[1::] + nextchar
            if lasttwo == '\n':
                return answer.decode(self.__ENCODING)

    def transmit(self, command):
        self.__port.reset_input_buffer()
        self.__port.write(command.encode(self.__ENCODING))

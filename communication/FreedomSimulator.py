import serial
from Language import Commands
import time

"""
This class should simulate the Freedomboard to test the communication without additional hardware
"""
class FreedomSimulator:
    # Settings for the serial port
    __PORT = '/dev/serial0'
    __BAUDRATE = 19200
    __BYTESIZE = serial.EIGHTBITS
    __PARITY = serial.PARITY_NONE
    __STOPBITS = serial.STOPBITS_ONE
    __TIMEOUT = 0

    # Other local vars
    __port = None

    def __init__(self):
        self.__port = serial.Serial(port=__PORT, baudrate=__BAUDRATE, bytesize=__BYTESIZE, parity=__PARITY, stopbits=__STOPBITS)

    def start(self):
        self.__port.open()
        simulation()

    def simulation(self):
        while True:
            received = self.__port.read()
            received += self.__port.readall()
            if received == Commands.INIT_COMMUNICATION:
                self.__port.write(b'ok')
                time.sleep(1)
                self.__port.write(b'finish')

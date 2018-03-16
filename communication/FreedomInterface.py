import serial

class FreedomInterface:
    # Here will be the instance stored.
    __instance = None
    __port = None

    # Settings for the serial port
    __PORT = '/dev/serial0'
    __BAUDRATE = 19200
    __BYTESIZE = serial.EIGHTBITS
    __PARITY = serial.PARITY_NONE
    __STOPBITS = serial.STOPBITS_ONE
    __TIMEOUT = 0

    @staticmethod
    def getInstance():
        """ Static access method. """
        if FreedomInterface.__instance == None:
            FreedomInterface()
        return FreedomInterface.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if FreedomInterface.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            FreedomInterface.__instance = self
            FreedomInterface.__port = serial.Serial(port=__PORT, baudrate=__BAUDRATE, bytesize=__BYTESIZE, parity=__PARITY, stopbits=__STOPBITS)

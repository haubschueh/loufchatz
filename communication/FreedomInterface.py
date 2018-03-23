from communication.Language import Commands
from communication.SerialCommunicator import SerialCommunicator

"""
This class represents the Freedom Board in our code.
It handles the flow of each command that can be given to the Freedom Board.
To keep the communication as simple as possible, there is no parallelism allowed.

Initialisation example:
>> frdm = FreedomInterface.getInstance()
"""
class FreedomInterface:
    # Here will be the instance stored.
    __instance = None
    __serialCommunicator = None

    @staticmethod
    def getInstance():
        # Static access method.
        if FreedomInterface.__instance == None:
            FreedomInterface()
        return FreedomInterface.__instance

    # This constructor would be private if he could.
    def __init__(self):
        if FreedomInterface.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            FreedomInterface.__instance = self
            FreedomInterface.__serialCommunicator = SerialCommunicator.getInstance()

    def __ackLoop(self, command):
        ack = ""
        while ack != Commands.ACKNOWLEDGE:
            self.__serialCommunicator.transmit(command)
            ack = self.__serialCommunicator.receive()

    def hello(self):
        while True:
            self.__serialCommunicator.transmit(Commands.HELLO)
            ack = self.__serialCommunicator.receive()
            if ack == Commands.ACKNOWLEDGE:
                break

    def drive(self):
        ack = ""
        while ack != Commands.ACKNOWLEDGE:
            self.__serialCommunicator.transmit(Commands.DRIVE)
            ack = self.__serialCommunicator.receive()

    def goto_cube(self):
        self.__serialCommunicator.transmit(Commands.GO_DISTANCE)

    def lift_cube(self):
        self.__ackLoop(Commands.LIFT_LOAD)
        fin = ""
        while fin != Commands.FINISHED:
            fin = self.__serialCommunicator.receive()

    def put_cube(self):
        self.__serialCommunicator.transmit(Commands.PUT_LOAD)

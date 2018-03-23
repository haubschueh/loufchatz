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

    def __waitForAck(self):
        ack = ""
        while ack != Commands.ACKNOWLEDGE:
            ack = self.__serialCommunicator.receive()

    def __waitForAnswer(self):
        while True:
            ack = self.__serialCommunicator.receive()
            if ack == Commands.ACKNOWLEDGE:
                break

    """
    Initialize the communication and handles the start signal.
    """
    def hello(self):
        self.__serialCommunicator.transmit(Commands.HELLO)
        self.__waitForAnswer()
        # wait for start signal

    """
    Commands to drive, stop and let the robot drive a fix distance.
    """
    def drive(self):
        self.__serialCommunicator.transmit(Commands.DRIVE)
        self.__waitForAck()

    def stop(self):
        self.__serialCommunicator.transmit(Commands.STOP)
        self.__waitForAck()

    def goto_cube(self):
        self.__serialCommunicator.transmit(Commands.GO_DISTANCE)
        self.__waitForAck()
        # wait for finish signal

    """
    Commands to lift and lower the payload.
    """
    def lift_cube(self):
        self.__ackLoop(Commands.LIFT_LOAD)
        self.__waitForAnswer()
        # wait for finish signal

    def put_cube(self):
        self.__serialCommunicator.transmit(Commands.PUT_LOAD)
        self.__waitForAnswer()
        # wait for finish signal

    """
    Gets the coordinates from the cube.
    """
    def position(self):
        self.__ackLoop(Commands.POSITION)
        self.__waitForAnswer()
        # get Position Data

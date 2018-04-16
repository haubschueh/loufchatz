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

    """
    Commands to drive forward, drive backward and stop.
    """
    def drive(self):
        self.__serialCommunicator.transmit(Commands.DRIVE)

    def driveSlow(self):
        self.__serialCommunicator.transmit(Commands.DRIVE_SLOW)

    def driveFast(self):
        self.__serialCommunicator.transmit(Commands.DRIVE_FAST)

    def stop(self):
        self.__serialCommunicator.transmit(Commands.STOP)

    def driveBackwardSlow(self):
        self.__serialCommunicator.transmit(Commands.BACKWARD_SLOW)

    def driveBackwardFast(self):
        self.__serialCommunicator.transmit(Commands.BACKWARD_FAST)

    """
    Gets the coordinates from the cube.
    """
    def getCubePosition(self):
        self.__serialCommunicator.transmit(Commands.POS_X)
        x = self.__serialCommunicator.receive()
        self.__serialCommunicator.transmit(Commands.POS_Z)
        z = self.__serialCommunicator.receive()
        return x

    def getState(self):
        self.__serialCommunicator.transmit('state')
        return self.__serialCommunicator.receive()

    def wait(self):
        ans = ""
        while ans != Commands.FRDM_START:
            ans = self.__serialCommunicator.receive()

    def cube(self):
        ans = ""
        while ans != Commands.FRDM_CUBEUP:
            ans = self.__serialCommunicator.receive()

    def finish(self):
        self.__serialCommunicator.transmit(Commands.FINISH)

from log.LoggerFactory import LoggerFactory
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
    __log = LoggerFactory.getLogger('FreedomInterface')

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
        self.__log.info('Move forward normal')
        self.__serialCommunicator.transmit(Commands.DRIVE)

    def driveSlow(self):
        self.__serialCommunicator.transmit(Commands.DRIVE_SLOW)

    def driveFast(self):
        self.__serialCommunicator.transmit(Commands.DRIVE_FAST)

    def stop(self):
        self.__log.info('Stop driving')
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
        self.__log.info('Waiting for the start signal')
        ans = ""
        while ans != Commands.FRDM_START:
            ans = self.__serialCommunicator.receive()
        self.__log.warning('Start signal received!')

    def cube(self):
        self.__log.info('Waiting for the FRDM to takt up the cube')
        ans = ""
        while ans != Commands.FRDM_CUBEUP:
            ans = self.__serialCommunicator.receive()
        self.__log.warning('Cube taken up. Raspi overtakes the control.')

    def finish(self):
        self.__log.warning('Put the cube down and finish the parcours.')
        self.__serialCommunicator.transmit(Commands.FINISH)

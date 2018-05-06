from log.LoggerFactory import LoggerFactory
from communication.Language import Commands
from communication.SerialCommunicator import SerialCommunicator
import Pyro4

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
        daemon = Pyro4.Daemon(host="192.168.10.8", port=34383)
        uri = daemon.register(FreedomInterface)
        self.__log.info("Pyro ready. Object uri =", uri)
        daemon.requestLoop()

    """
    Language commands implementations.
    """
    def waitForStart(self):
        self.__log.info('Waiting for the start signal')
        ans = ""
        while ans != Commands.FRDM_START:
            ans = self.__serialCommunicator.receive()
        self.__log.warning('Start signal received!')

    def waitForCube(self):
        self.__log.info('Waiting for the FRDM to takt up the cube')
        ans = ""
        while ans != Commands.FRDM_CUBEUP:
            ans = self.__serialCommunicator.receive()
        self.__log.warning('Cube taken up. Raspi overtakes the control.')

    def finish(self):
        self.__log.warning('Put the cube down and finish the parcours.')
        self.__serialCommunicator.transmit(Commands.FINISH)

    def getCubePositionX(self):
        self.__serialCommunicator.transmit(Commands.POS_X)
        x = self.__serialCommunicator.receive()
        return x

    def getCubePositionZ(self):
        self.__serialCommunicator.transmit(Commands.POS_Z)
        z = self.__serialCommunicator.receive()
        return z

    def getState(self):
        self.__serialCommunicator.transmit(Commands.STATE)
        return self.__serialCommunicator.receive()

    def drive(self):
        self.__log.info('Move forward normal')
        self.__serialCommunicator.transmit(Commands.FORWARD)

    def driveSlow(self):
        self.__serialCommunicator.transmit(Commands.FORWARD_SLOW)

    def driveFast(self):
        self.__serialCommunicator.transmit(Commands.FORWARD_FAST)

    def driveBackward(self):
        self.__serialCommunicator.transmit(Commands.BACKWARD)

    def driveBackwardSlow(self):
        self.__serialCommunicator.transmit(Commands.BACKWARD_SLOW)

    def driveBackwardFast(self):
        self.__serialCommunicator.transmit(Commands.BACKWARD_FAST)

    def stop(self):
        self.__log.info('Stop driving')
        self.__serialCommunicator.transmit(Commands.STOP)

    def hopperUp(self):
        self.__log.info('Move forward normal')
        self.__serialCommunicator.transmit(Commands.HOPPER_UP)

    def hopperDown(self):
        self.__serialCommunicator.transmit(Commands.HOPPER_DOWN)

    def hopperStop(self):
        self.__serialCommunicator.transmit(Commands.HOPPER_STOP)

    def attachCube(self):
        self.__serialCommunicator.transmit(Commands.ATTACH_CUBE)

    def releaseCube(self):
        self.__serialCommunicator.transmit(Commands.RELEASE_CUBE)

    """
    Debug commands.
    """
    def reset(self):
        self.__serialCommunicator.transmit(Commands.RESET)
        return self.__serialCommunicator.receive()

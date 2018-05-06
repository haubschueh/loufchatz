from communication.FreedomInterface import FreedomInterface
import Pyro4

@Pyro4.expose
class PyroFacade:
    __FreedomInterface = None

    def __init__(self):
        self.__FreedomInterface = FreedomInterface.getInstance()

    def getCubePositionX(self):
        x = self.__FreedomInterface.getCubePositionX()
        return x

    def getCubePositionZ(self):
        z = self.__FreedomInterface.getCubePositionZ()
        return z

    def getState(self):
        s = self.__FreedomInterface.getState()
        return s

    def drive(self):
        self.__FreedomInterface.drive()

    def driveSlow(self):
        self.__FreedomInterface.driveSlow()

    def driveFast(self):
        self.__FreedomInterface.driveFast()

    def driveBackward(self):
        self.__FreedomInterface.driveBackward()

    def driveBackwardSlow(self):
        self.__FreedomInterface.driveBackwardSlow()

    def driveBackwardFast(self):
        self.__FreedomInterface.driveBackwardFast()

    def stop(self):
        self.__FreedomInterface.stop()

    def hopperUp(self):
        self.__FreedomInterface.hopperUp()

    def hopperDown(self):
        self.__FreedomInterface.hopperDown()

    def hopperStop(self):
        self.__FreedomInterface.hopperStop()

    def attachCube(self):
        self.__FreedomInterface.attachCube()

    def releaseCube(self):
        self.__FreedomInterface.releaseCube()

    def reset(self):
        a = self.__FreedomInterface.reset()
        return a

from communication.FreedomInterface import FreedomInterface
import Pyro4

class PyroFacade:
    self.__FreedomInterface = None

    def __init__(self):
        self.__FreedomInterface = FreedomInterface.getInstance()

    @Pyro4.expose
    def getCubePositionX(self):
        x = self.__FreedomInterface.getCubePositionX()
        return x

    @Pyro4.expose
    def getCubePositionZ(self):
        z = self.__FreedomInterface.getCubePositionZ()
        return z

    @Pyro4.expose
    def getState(self):
        s = self.__FreedomInterface.getState()
        return s

    @Pyro4.expose
    def drive(self):
        self.__FreedomInterface.drive()

    @Pyro4.expose
    def driveSlow(self):
        self.__FreedomInterface.driveSlow()

    @Pyro4.expose
    def driveFast(self):
        self.__FreedomInterface.driveFast()

    @Pyro4.expose
    def driveBackward(self):
        self.__FreedomInterface.driveBackward()

    def driveBackwardSlow(self):
        self.__FreedomInterface.driveBackwardSlow()

    @Pyro4.expose
    def driveBackwardFast(self):
        self.__FreedomInterface.driveBackwardFast()

    @Pyro4.expose
    def stop(self):
        self.__FreedomInterface.stop()

    @Pyro4.expose
    def hopperUp(self):
        self.__FreedomInterface.hopperUp()

    @Pyro4.expose
    def hopperDown(self):
        self.__FreedomInterface.hopperDown()

    @Pyro4.expose
    def hopperStop(self):
        self.__FreedomInterface.hopperStop()

    @Pyro4.expose
    def attachCube(self):
        self.__FreedomInterface.attachCube()

    @Pyro4.expose
    def releaseCube(self):
        self.__FreedomInterface.releaseCube()

    @Pyro4.expose
    def reset(self):
        a = self.__FreedomInterface.reset()
        return a

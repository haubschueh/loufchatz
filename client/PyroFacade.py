from communication.FreedomInterface import FreedomInterface
#from targetrecognition.targetrec import TargetRec
from client.beginLogic import BeginLogic
import Pyro4

@Pyro4.expose
class PyroFacade:
    __FreedomInterface = None
    __X = -1
    __Z = -1

    def __init__(self):
        self.__FreedomInterface = FreedomInterface.getInstance()
        #self.targetRec = TargetRec()
        #self.beginLogic = BeginLogic()

    #def searchTargetPlate(self):
        #self.targetRec.searchSquare()

    #def startRun(self):
        #self.beginLogic.start()

    #def letsGo(self):
        #return self.beginLogic.getLetsGo()

    #def waitForCube(self):
        #self.__FreedomInterface.waitForCube()

    #def finish(self):
        #self.__FreedomInterface.finish()

    def setX(self, newVar):
        self.__X = newVar

    def setZ(self, newVar):
        self.__Z = newVar

    def getCubePositionX(self):
        if self.__X == -1:
            x = self.__FreedomInterface.getCubePositionX()
        else:
            x = self.__X
        return x

    def getCubePositionZ(self):
        if self.__Z == -1:
            z = self.__FreedomInterface.getCubePositionZ()
        else:
            z = self.__Z
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

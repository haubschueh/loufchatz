#from log.LoggerFactory import LoggerFactory
#from communication.FreedomInterface import FreedomInterface
import time
import threading

"""

"""

class PositionUpdater(threading.Thread):
    #log = LoggerFactory.getLogger('Position')
    #freedomBoard = FreedomInterface.getInstance()
    alive = False

    def __init__(self, logger, frdm):
        threading.Thread.__init__(self)
        self.log = logger
        self.freedomBoard = frdm

    def run(self):
        while(self.alive):
            x = self.freedomBoard.getCubePositionX()
            z = self.freedomBoard.getCubePositionZ()
            self.log.info('CubePosition is: X=%i, Z=%i', x, z)
            s = self.freedomBoard.getState()
            self.log.info('Freedom State is: X=%i', s)
            time.sleep(1)

    def stop(self):
        self.alive = False

from log.LoggerFactory import LoggerFactory
from communication.FreedomInterface import FreedomInterface
import time

"""

"""

class PositionUpdater:
    log = LoggerFactory.getLogger('Position')
    freedomBoard = FreedomInterface.getInstance()
    alive = False

    def start(self):
        alive = True
        while(alive):
            x = freedomBoard.getCubePositionX()
            z = freedomBoard.getCubePositionZ()
            log.info('CubePosition is: X=%i, Z=%i', x, z)
            time.sleep(1)

    def stop(self):
        alive = False

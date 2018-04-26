from log.LoggerFactory import LoggerFactory
from communication.FreedomInterface import FreedomInterface
import time
import threading

"""

"""

class PositionUpdater(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        log = LoggerFactory.getLogger('Position')
        freedomBoard = FreedomInterface.getInstance()
        alive = False

    def run(self):
        while(alive):
            x = freedomBoard.getCubePositionX()
            z = freedomBoard.getCubePositionZ()
            log.info('CubePosition is: X=%i, Z=%i', x, z)
            s = freedomBoard.getState()
            log.info('Freedom State is: X=%i', s)
            time.sleep(1)

    def stop(self):
        alive = False

from log.LoggerFactory import LoggerFactory
from communication.FreedomInterface import FreedomInterface
from targetrecognition.targetrec import TargetRec
from position.Position import PositionUpdater
import time

"""

"""
log = LoggerFactory.getLogger('main')
freedomBoard = FreedomInterface.getInstance()
targetRec = TargetRec()
positionUpdater = PositionUpdater()

log.info('Run started.')
freedomBoard.waitForStart()
freedomBoard.waitForCube()
#Continues to run when the target is found
positionUpdater.start()
freedomBoard.drive()
targetRec.searchSquare()
freedomBoard.stop()
time.sleep(.300)
freedomBoard.finish()
log.info('Run finished.')
log.info('Raspi goes to sleep.')

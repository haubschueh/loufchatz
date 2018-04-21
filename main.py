from log.LoggerFactory import LoggerFactory
from communication.FreedomInterface import FreedomInterface
from targetrecognition.targetrec import TargetRec
#from position.Position import Position
import time

"""

"""
log = LoggerFactory.getLogger('main')

#target_rec = TargetRec()
#pos_out = Position()
#__state = WaitForStartSignal()

freedomBoard = FreedomInterface.getInstance()
targetRec = TargetRec()

log.info('Run started.')
freedomBoard.wait()
freedomBoard.cube()
freedomBoard.drive()
#Continues to run when the target is found
targetRec.searchSquare()
freedomBoard.stop()
time.sleep(.300)
freedomBoard.finish()
log.info('Run finished.')
log.info('Raspi goes to sleep.')

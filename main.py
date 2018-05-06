from log.LoggerFactory import LoggerFactory
from communication.FreedomInterface import FreedomInterface
from targetrecognition.targetrec import TargetRec
#from position.position import PositionUpdater
from client.ClientInterface import ClientInterface
import time

"""

"""
log = LoggerFactory.getLogger('main')
freedomBoard = FreedomInterface.getInstance()
targetRec = TargetRec()
#positionUpdater = PositionUpdater(LoggerFactory.getLogger('Position'), freedomBoard)
clientInterface = ClientInterface()
uri = clientInterface.getUri()

log.info('Run started.')
log.info('Client uri is: %s', uri)
freedomBoard.waitForStart()
freedomBoard.waitForCube()
#Continues to run when the target is found
#positionUpdater.start()
freedomBoard.drive()
targetRec.searchSquare()
time.sleep(2.7)
freedomBoard.stop()
#positionUpdater.stop()
time.sleep(.300)
freedomBoard.finish()
log.info('Run finished.')
log.info('Raspi goes to sleep.')

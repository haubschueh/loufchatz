from log.LoggerFactory import LoggerFactory
from communication.FreedomInterface import FreedomInterface
from targetrecognition.targetrec import TargetRec
from client.ClientInterface import ClientInterface
import time

"""

"""
log = LoggerFactory.getLogger('main')
freedomBoard = FreedomInterface.getInstance()
targetRec = TargetRec()
#clientInterface = ClientInterface()
#uri = clientInterface.getUri()
#clientInterface.start()

log.info('Run started.')
#log.info('Client uri is: %s', uri)
freedomBoard.waitForStart()
freedomBoard.waitForCube()
freedomBoard.drive()
targetRec.searchSquare()
time.sleep(2.7)
freedomBoard.stop()
time.sleep(.300)
freedomBoard.finish()
log.info('Run finished.')
log.info('Raspi goes to sleep.')

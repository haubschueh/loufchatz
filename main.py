from log.LoggerFactory import LoggerFactory
from communication.FreedomInterface import FreedomInterface
from targetrecognition.targetrec import TargetRec
from client.ClientInterface import ClientInterface
from position.position import PositionUpdater
from client.PyroFacade import PyroFacade
import time

"""

"""
log = LoggerFactory.getLogger('main')
freedomBoard = FreedomInterface.getInstance()
targetRec = TargetRec()
pyroFacade = PyroFacade()
clientInterface = ClientInterface(pyroFacade)
uri = clientInterface.getUri()
clientInterface.start()
positionUpdater = PositionUpdater(freedomBoard, pyroFacade)

log.info('Run started.')
freedomBoard.reset()
log.info('Board resetted.')
log.info('Client uri is: %s', uri)
freedomBoard.waitForStart()
freedomBoard.waitForCube()
freedomBoard.driveFast()
positionUpdater.start()
targetRec.searchSquare()
#short 1.2
X = pyroFacade.getX()
timeToWait = 0.005 * int(X) + 0.9
print('Wait %s', timeToWait)
time.sleep(timeToWait)
#long 2.6
freedomBoard.stop()
positionUpdater.stop()
pyroFacade.setZ(4)
time.sleep(.300)
freedomBoard.finish()
log.info('Run finished.')
log.info('Raspi goes to sleep.')

from communication.FreedomInterface import FreedomInterface
from targetrecognition.targetrec import TargetRec
import time
#from targetrecognition.TargetRec import TargetRec
#from position.Position import Position

"""

"""

#target_rec = TargetRec()
#pos_out = Position()
#__state = WaitForStartSignal()

freedomBoard = FreedomInterface.getInstance()
targetRec = TargetRec()

freedomBoard.wait()
freedomBoard.cube()
freedomBoard.drive()
#Continues to run when the target is found
targetRec.searchSquare()
freedomBoard.stop()
time.sleep(.300)
freedomBoard.finish()

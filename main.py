from communication.FreedomInterface import FreedomInterface
import time
#from targetrecognition.TargetRec import TargetRec
#from position.Position import Position

"""

"""

#target_rec = TargetRec()
#pos_out = Position()
#__state = WaitForStartSignal()

freedomBoard = FreedomInterface.getInstance()

freedomBoard.wait()
freedomBoard.cube()
freedomBoard.drive()
time.sleep(5)
freedomBoard.stop()
time.sleep(.300)
freedomBoard.finish()

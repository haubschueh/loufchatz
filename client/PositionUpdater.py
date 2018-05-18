import threading
import time

class PositionUpdater(threading.Thread):
    def __init__(self, remoteClass, userInterface):
        threading.Thread.__init__(self)
        self.loufchatz = remoteClass
        self.gui = userInterface

    def run(self):
        while True:
            x = self.loufchatz.getCubePositionX()
            z = self.loufchatz.getCubePositionZ()
            self.gui.updatePosition(x, z)
            time.sleep(.250)

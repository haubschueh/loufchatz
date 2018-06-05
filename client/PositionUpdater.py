import threading
import time

class PositionUpdater(threading.Thread):
    def __init__(self, remoteClass, userInterface):
        threading.Thread.__init__(self)
        self.loufchatz = remoteClass
        self.gui = userInterface
        self.updatePosition = True
        #self.gui.updatePosition("-", "-")

    def run(self):
        while True:
            if self.updatePosition:
                x = self.loufchatz.getCubePositionX()
                z = self.loufchatz.getCubePositionZ()
                self.gui.updatePosition(x, z)
                time.sleep(.250)

    def getUpdatingPosition(self):
        return self.updatePosition

    def setUpdatingPosition(self, value):
        self.updatePosition = value

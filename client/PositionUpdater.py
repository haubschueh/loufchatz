import threading
import time

class PositionUpdater(threading.Thread):
    def __init__(self, remoteClass, userInterface):
        threading.Thread.__init__(self)
        self.loufchatz = remoteClass
        self.gui = userInterface
        self.updatePosition = True

    def run(self):
        while True:
            if updatePosition:
                x = self.loufchatz.getCubePositionX()
                z = self.loufchatz.getCubePositionZ()
                self.gui.updatePosition(x, z)
                time.sleep(.250)

    def disableUpdatingPosition():
        self.updatePosition = False

    def enableUpdatingPosition():
        self.updatePosition = True

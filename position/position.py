from communication.FreedomInterface import FreedomInterface
from client.PyroFacade import PyroFacade
import time
import threading

"""
"""
class PositionUpdater(threading.Thread):
    alive = True

    def __init__(self, frdm, client):
        threading.Thread.__init__(self)
        self.freedomBoard = frdm
        self.client = client
        x = self.freedomBoard.getCubePositionX()
        z = self.freedomBoard.getCubePositionZ()
        self.client.setX(x)
        self.client.setZ(z)

    def run(self):
        while(self.alive):
            x = self.freedomBoard.getCubePositionX()
            z = self.freedomBoard.getCubePositionZ()
            self.client.setX(x)
            self.client.setZ(z)
            time.sleep(0.1)

    def stop(self):
        self.alive = False

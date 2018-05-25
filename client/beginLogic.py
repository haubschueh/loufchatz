import threading
from communication.FreedomInterface import FreedomInterface

class BeginLogic(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.letsGo = False

    def run(self):
        self.__FreedomInterface.waitForStart()
        self.__FreedomInterface.waitForCube()
        self.letsGo = True

    def getLetsGo(self):
        return self.letsGo

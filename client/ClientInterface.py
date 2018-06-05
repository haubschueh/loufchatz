from client.PyroFacade import PyroFacade
import threading
import Pyro4
import os

"""

"""
class ClientInterface(threading.Thread):

    __daemon = None
    __IP = os.popen('ip addr show wlan0').read().split("inet ")[1].split("/")[0]
    __PORT = 34383
    __pyroUri = ""

    def __init__(self, remoteObject):
        threading.Thread.__init__(self)
        pyroFacade = remoteObject
        self.daemon = Pyro4.Daemon(host=self.__IP, port=self.__PORT)
        self.pyroUri = self.daemon.register(pyroFacade)

    def run(self):
        self.daemon.requestLoop()

    def getUri(self):
        return self.pyroUri

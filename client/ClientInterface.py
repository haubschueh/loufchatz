from client.PyroFreedomInterfaceFacade import PyroFacade
import threading
import Pyro4

"""

"""
class ClientInterface(threading.Thread):

    __daemon = None
    __IP = "192.168.10.8"
    __PORT = 34383
    __pyroUri = ""

    def __init__(self):
        threading.Thread.__init__(self)
        pyroFacade = PyroFacade()
        self.daemon = Pyro4.Daemon(host=__IP, port=__PORT)
        self.pyroUri = self.daemon.register(pyroFacade)

    def run(self):
        self.daemon.requestLoop()

    def getUri(self):
        return self.pyroUri

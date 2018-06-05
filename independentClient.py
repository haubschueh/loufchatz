from client.ClientInterface import ClientInterface
from client.PyroFacade import PyroFacade
import time

pyroFacade = PyroFacade()
clientInterface = ClientInterface(pyroFacade)
uri = clientInterface.getUri()
clientInterface.start()
print('Client uri is: %s', uri)
while True:
    time.sleep(1)

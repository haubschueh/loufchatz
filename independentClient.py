from client.ClientInterface import ClientInterface
import time

clientInterface = ClientInterface()
uri = clientInterface.getUri()
clientInterface.start()
print('Client uri is: %s', uri)
while True:
    time.sleep(1)

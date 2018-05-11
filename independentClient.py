from client.ClientInterface import ClientInterface
clientInterface = ClientInterface()
uri = clientInterface.getUri()
clientInterface.start()
print('Client uri is: %s', uri)

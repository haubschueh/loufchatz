import Pyro4

uri = input("192.168.10.8").strip()
name = input("Marco").strip()

greeting_maker = Pyro4.Proxy(uri)         # get a Pyro proxy to the greeting object
print(greeting_maker.get_fortune(name))   # call method normally

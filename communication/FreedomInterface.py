from communication.Language import Commands
from communication.SerialCommunicator import SerialCommunicator

"""
This class represents the Freedom Board in our code.
It handles the flow of each command that can be given to the Freedom Board.
To keep the communication as simple as possible, there is no parallelism allowed.

Initialisation example:
>> frdm = FreedomInterface.getInstance()
"""
class FreedomInterface:
    # Here will be the instance stored.
    __instance = None
    __serialCommunicator = None

    @staticmethod
    def getInstance():
        # Static access method.
        if FreedomInterface.__instance == None:
            FreedomInterface()
        return FreedomInterface.__instance

    # This constructor would be private if he could.
    def __init__(self):
        if FreedomInterface.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            FreedomInterface.__instance = self
            FreedomInterface.__serialCommunicator = SerialCommunicator.getInstance()

    def __waitForAck(self):
        ack = ""
        while ack != Commands.ACKNOWLEDGE:
            ack = self.__serialCommunicator.receive()
        # while True:
        #     ack = self.__serialCommunicator.receive()
        #     if ack == Commands.ACKNOWLEDGE:
        #         break

    def __waitForFin(self):
        fin = ""
        while fin != Commands.FINISHED:
            fin = self.__serialCommunicator.receive()

    """
    Initialize the communication and handles the start signal.
    """
    def hello(self):
        self.__serialCommunicator.transmit(Commands.HELLO)
        self.__waitForAck()
        # wait for start signal
        self.__waitForFin()

    """
    Commands to drive, stop and let the robot drive a fix distance.
    """
    def drive(self):
        self.__serialCommunicator.transmit(Commands.DRIVE)
        #self.__waitForAck()

    def driveSlow(self):
        self.__serialCommunicator.transmit(Commands.DRIVE_SLOW)
        #self.__waitForAck()

    def driveFast(self):
        self.__serialCommunicator.transmit(Commands.DRIVE_FAST)
        #self.__waitForAck()

    def stop(self):
        self.__serialCommunicator.transmit(Commands.STOP)
        #self.__waitForAck()

    def goto_cube(self):
        self.__serialCommunicator.transmit(Commands.GO_DISTANCE)
        self.__waitForAck()
        self.__waitForFin()

    """
    Commands to lift and lower the payload.
    """
    def lift_cube(self):
        self.__serialCommunicator.transmit(Commands.LIFT_LOAD)
        self.__waitForAck()
        self.__waitForFin()

    def put_cube(self):
        self.__serialCommunicator.transmit(Commands.PUT_LOAD)
        self.__waitForAck()
        self.__waitForFin()

    """
    Gets the coordinates from the cube.
    """
    def getCubePosition(self):
        self.__serialCommunicator.transmit(Commands.POS_X)
        x = self.__serialCommunicator.receive()
        self.__serialCommunicator.transmit(Commands.POS_Z)
        z = self.__serialCommunicator.receive()
        return x

    def wait(self):
        ans = ""
        while ans != Commands.FRDM_START:
            ans = self.__serialCommunicator.receive()

    def cube(self):
        ans = ""
        while ans != Commands.FRDM_CUBEUP:
            ans = self.__serialCommunicator.receive()

    def finish(self):
        self.__serialCommunicator.transmit(Commands.FINISH)
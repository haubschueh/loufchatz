"""
Commands and values used for serial communication

Usage example:
>> Commands.EMERGENCY
b'kill'
"""
class Commands():
    INIT_COMMUNICATION  = b'hello'
    GO_DISTANCE         = b'distance'
    LIFT_LOAD           = b'loadup'
    DRIVE               = b'drive'
    STOP                = b'stop'
    LOWER_LOAD          = b'loaddown'
    EMERGENCY           = b'kill'
    POSITION            = b'position'

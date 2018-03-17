"""
Commands and values used for serial communication

Usage example:
>> Commands.EMERGENCY
b'kill'
"""
class Commands():
    HELLO       = 'hello'
    GO_DISTANCE = 'distance'
    LIFT_LOAD   = 'loadup'
    DRIVE       = 'drive'
    STOP        = 'stop'
    LOWER_LOAD  = 'loaddown'
    EMERGENCY   = 'kill'
    POSITION    = 'position'

"""
Commands and values used for serial communication

Usage example:
>> Commands.EMERGENCY
'kill'
"""
class Commands():
    HELLO       = 'hello'
    DRIVE       = 'drive'
    STOP        = 'stop'
    GO_DISTANCE = 'distance'
    LIFT_LOAD   = 'loadup'
    PUT_LOAD    = 'loaddown'
    POSITION    = 'position'
    ACKNOWLEDGE = 'ok'
    FINISHED    = 'finish'
    END_SIGN    = '\n'
    EMERGENCY   = 'kill'

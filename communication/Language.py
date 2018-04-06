"""
Commands and values used for serial communication

Usage example:
>> Commands.EMERGENCY
'kill'
"""
class Commands():
    HELLO       = 'hello'
    GO_DISTANCE = 'distance'
    LIFT_LOAD   = 'loadup'
    PUT_LOAD    = 'loaddown'
    ACKNOWLEDGE = 'ok'
    EMERGENCY   = 'kill'
    END_SIGN        = '\n'
    FRDM_START      = 'start'
    FRDM_CUBEUP     = 'cube attached'
    POS_X           = 'x'
    POS_Z           = 'z'
    DRIVE           = 'f7'
    DRIVE_SLOW      = 'f3'
    DRIVE_FAST      = 'f10'
    STOP            = 'f0'
    FINISH          = 'deliver'

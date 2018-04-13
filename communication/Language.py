"""
Commands and values used for serial communication

Usage example:
>> Commands.EMERGENCY
'kill'
"""
class Commands():
    END_SIGN        = '\n'
    FRDM_START      = 'we go'
    FRDM_CUBEUP     = 'raspi you go'
    POS_X           = 'x'
    POS_Z           = 'z'
    DRIVE           = 'f7'
    DRIVE_SLOW      = 'f3'
    DRIVE_FAST      = 'f10'
    STOP            = 'f0'
    FINISH          = 'deliver'

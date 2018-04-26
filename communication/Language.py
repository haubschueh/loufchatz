"""
Commands and values used for serial communication

Usage example:
>> Commands.ATTACH_CUBE
'attach'
"""
class Commands():
    END_SIGN        = '\n'
    FRDM_START      = 'we go'
    FRDM_CUBEUP     = 'raspi you go'
    RESET           = 'reset'
    STATE           = 'state'
    POS_X           = 'x'
    POS_Z           = 'z'
    FORWARD         = 'f7'
    FORWARD_SLOW    = 'f3'
    FORWARD_FAST    = 'f10'
    BACKWARD        = 'b7'
    BACKWARD_SLOW   = 'b3'
    BACKWARD_FAST   = 'b10'
    STOP            = 'f0'
    HOPPER_UP       = 'u3'
    HOPPER_DOWN     = 'd3'
    HOPPER_STOP     = 'd0'
    ATTACH_CUBE     = 'attach'
    RELEASE_CUBE    = 'release'
    FINISH          = 'deliver'

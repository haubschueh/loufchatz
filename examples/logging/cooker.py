import logging

log = logging.getLogger('cooker')
temperature = 115

def first():
    log.info('Hi, I\'m the cooker')

def second():
    log.warning('It gets to hot here')
    log.debug('Temp is: %i', temperature)

def third():
    log.critical('BOOM!!!')

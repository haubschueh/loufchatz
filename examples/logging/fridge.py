import logging

log = logging.getLogger('fridge')
friend = 'cooker'

def first():
    log.info('Hi, I\'m the fridge')

def second():
    log.warning('Some strange things happen near my place')

def third():
    log.error('OMG, the %s exploded!', friend)

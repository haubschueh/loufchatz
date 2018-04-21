import fridge
import cooker
from LoggerFactory import LoggerFactory

log = LoggerFactory.getLogger('main')

log.info('Log started.')
fridge.first()
cooker.first()
fridge.second()
cooker.second()
cooker.third()
fridge.third()
log.info('Log stopped.')

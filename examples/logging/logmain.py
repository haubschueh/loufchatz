import logging
import fridge
import cooker

logging.basicConfig(filename='example.log', filemode='w', format='%(asctime)s %(levelname)s %(name)s %(message)s', datefmt='%H:%M:%S')

fridge.first()
cooker.first()
fridge.second()
cooker.second()
cooker.third()
fridge.third()

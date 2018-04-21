import logging
import datetime as dt

class LoggerFactory:

    @staticmethod
    def getLogger(name):

        formatter = customFormatter(format='%(asctime)s %(levelname)-8s %(name)s %(message)s', datefmt = '%Y-%m-%d,%H:%M:%S.%f')

        logger = logging.getLogger('simple_example')
        logger.setLevel(logging.DEBUG)

        consoleHandler = logging.StreamHandler(stream=sys.stderr)
        consoleHandler.setLevel(logging.DEBUG)
        consoleHandler.setFormatter(formatter)

        fileHandler = logging.FileHandler('example.log', mode='w')
        fileHandler.setLevel(logging.DEBUG)
        fileHandler.setFormatter(formatter)

        logger.addHandler(consoleHandler)
        return logger

class customFormatter(logging.Formatter):
    converter = dt.datetime.fromtimestamp
    def formatTime(self, record, datefmt = None):
        ct = self.converter(record.created)
        if datefmt:
            s = ct.strftime(datefmt)
        else:
            t = ct.strftime("%Y-%m-%d %H:%M:%S")
            s = "%s,%03d" % (t, record.msecs)
        return s

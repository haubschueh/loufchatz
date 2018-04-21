import logging
import datetime as dt

class LoggerFactory:
    consoleHandler = None
    fileHandler = None

    @staticmethod
    def getLogger(name):

        formatter = customFormatter(fmt='%(asctime)s %(levelname)-8s %(name)s %(message)s', datefmt = None)

        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        if LoggerFactory.consoleHandler == None:
            LoggerFactory.consoleHandler = logging.StreamHandler()
            LoggerFactory.consoleHandler.setLevel(logging.DEBUG)
            LoggerFactory.consoleHandler.setFormatter(formatter)

        if LoggerFactory.fileHandler == None:
            LoggerFactory.fileHandler = logging.FileHandler('example.log', mode='w')
            LoggerFactory.fileHandler.setLevel(logging.DEBUG)
            LoggerFactory.fileHandler.setFormatter(formatter)

        logger.addHandler(LoggerFactory.consoleHandler)
        logger.addHandler(LoggerFactory.fileHandler)
        return logger

class customFormatter(logging.Formatter):
    converter = dt.datetime.fromtimestamp
    def formatTime(self, record, datefmt = None):
        ct = self.converter(record.created)
        if datefmt:
            s = ct.strftime(datefmt)
        else:
            t = ct.strftime('%H:%M:%S')
            s = '%s.%03d' % (t, record.msecs)
        return s

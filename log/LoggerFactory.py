import logging
import datetime as dt

"""
Factory for logger objects.
Use this class to generate logger objects because this way it's possible to run multiple loghandlers and a custom logformatter.

Usage example:
>> from log.LoggerFactory import LoggerFactory

>> log = LoggerFactory.getLogger('main')
>> log.info('Here you write the information')
>> log.error('Here you write the error')
"""
class LoggerFactory:
    consoleHandler = None
    fileHandler = None
    logfilePath = './log/lastRun.log'

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
            LoggerFactory.fileHandler = logging.FileHandler(LoggerFactory.logfilePath, mode='w')
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

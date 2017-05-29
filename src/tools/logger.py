'''
    Logging utilities
'''

import logging
import os

from datetime import datetime

LOG = logging.getLogger('main')
LOGFILE = 'logs/log' + str(datetime.now())[0:16]

LOG.setLevel(logging.DEBUG)

DEBUG = True


def logWarning(msg):
    LOG.warning(msg)


def logDebug(msg):
    print(msg)


def logInfo(msg):
    print(msg)
    LOG.info(msg)


def logError(msg):
    LOG.error(msg)


logInfo('Logger initialized')

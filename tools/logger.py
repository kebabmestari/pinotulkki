'''
    Logging utilities
'''

import logging
import os

from datetime import datetime

ROOTDIR = os.path.dirname(os.path.abspath(__file__))

LOG = logging
LOGFILE = '../logs/pinotulkki_log' + str(datetime.now())

LOG.basicConfig(filename=LOGFILE, level=logging.DEBUG)


def logWarning(msg):
    LOG.warning(msg)


def logDebug(msg):
    LOG.debug(msg)


def logInfo(msg):
    LOG.info(msg)


def logError(msg):
    LOG.error(msg)


logInfo('Logger initialized')

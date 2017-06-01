'''
    Logging utilities
'''

import logging
from imp import reload
reload(logging)
import os

from datetime import datetime

LOGDIR = 'logs'
ROOTPATH = ''

if os.path.exists(LOGDIR) and os.path.isdir(LOGDIR):
    ROOTPATH = LOGDIR + '/'
LOGFILE = ROOTPATH + 'log' + str(datetime.now())[0:16]

LOG = logging.getLogger()  # root logger

fileHandler = logging.FileHandler(LOGFILE)
consoleHandler = logging.StreamHandler()

LOG.addHandler(fileHandler)
LOG.addHandler(consoleHandler)

LOG.setLevel(logging.DEBUG)


def log_warning(msg):
    LOG.warning('WARNING: ' + msg)


def log_debug(msg):
    LOG.debug('DEBUG: ' + msg)


def log_info(msg):
    LOG.info('INFO: ' + msg)


def log_error(msg):
    LOG.error('ERROR: ' + msg)


def log_result(value):
    LOG.info('RESULT: ' + str(value))


def end_logging():
    log_debug('Shutting down logger')
    logging.shutdown()


log_debug('Logger initialized')
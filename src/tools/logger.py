'''
    Logging utilities
'''

import logging
import os
from datetime import datetime

from common import constants

LOG_DIR = 'logs'
ROOT_PATH = ''

if os.path.exists(LOG_DIR) and os.path.isdir(LOG_DIR):
    ROOT_PATH = LOG_DIR + '/'
LOGFILE = ROOT_PATH + 'log' + str(datetime.now())[0:16].replace(' ', '-').replace(':', '-')

LOG = logging.getLogger()  # root logger

fileHandler = logging.FileHandler(LOGFILE)
consoleHandler = logging.StreamHandler()

LOG.addHandler(fileHandler)

LOG.setLevel(logging.DEBUG)

# If debugging is on, log everything to console too
# If not, debug log goes only into file
if constants.DEBUG:
    LOG.addHandler(consoleHandler)


def log_warning(msg):
    LOG.warning('WARNING: ' + msg)


def log_debug(msg):
    LOG.debug('DEBUG: ' + msg)


def log_graphics(msg):
    LOG.debug('GFX: ' + msg)


def log_info(msg):
    LOG.info('INFO: ' + msg)


def log_error(msg):
    LOG.error('ERROR: ' + msg)
    print('ERROR: ' + msg)


def log_result(value):
    LOG.debug('RESULT: ' + str(value))


def log_print(value):
    LOG.info('PRINT: ' + str(value))
    print('PRINT: ' + str(value))


def end_logging():
    log_debug('Shutting down logger')
    logging.shutdown()


log_debug('Logger initialized')

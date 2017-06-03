from common import constants
from tools import logger

#  Print
def print_handler(value):
    logger.log_print(str(value).replace(constants.STRING_WHITESPACE, ' '))

# Read
def read_handler():
    return input(': ')
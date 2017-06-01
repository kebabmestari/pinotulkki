from tools import logger

#  Print
def print_handler(value):
    logger.log_result(value)

# Read
def read_handler():
    return input(': ')
from tools import logger

#  Print
def print_handler(value):
    logger.log_print(value)

# Read
def read_handler():
    return input(': ')
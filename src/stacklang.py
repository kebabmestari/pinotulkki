#!/usr/bin/python3

'''
    Stack interpreter
    For course Ohjelmointikielet ja paradigmat
    University of Turku
    
    Samuel Lindqvist
    Juha-Pekka Samuelsson
    Lassi Salomaa
'''
import os
import sys

from common import constants
from runtime import interpreter
from runtime import scopeservice
from tools import logger
from tools import parser
from tools import reader

DEFAULT_FILE = 'laskuja.txt'
PROGRAM_NAME = 'PINOTULKKI'

_file_rows = []  # input file lines
_input_tokens = []  # input tokens

_global_scope = scopeservice.create_scope('global scope', -1)
_instr_stack = scopeservice.get_instr_stack(_global_scope['id'])  # Instructions stack
_data_stack = scopeservice.get_data_stack(_global_scope['id'])  # Data stack


# Program entry point
def main(args):
    global _file_rows
    global _input_tokens
    global _instr_stack
    global _data_stack

    input_file = ''

    if len(args) == 0:
        logger.log_info('No input file given, defaulting to ' + DEFAULT_FILE)
        input_file = DEFAULT_FILE
    else:
        input_file = args[0]

    logger.log_info('%s started' % PROGRAM_NAME)
    logger.log_info('Input file: ' + input_file)

    try:
        _file_rows = reader.readfile(os.getcwd(), input_file)
    except FileNotFoundError:
        logger.log_error('File does not exists')
        return
    except IOError:
        logger.log_error('IO error while reading input file')
        return

    logger.log_info('File read')
    logger.log_info('Parsing tokens')

    # Break file into singular tokens
    _input_tokens = parser.break_lines(_file_rows)

    logger.log_info('Tokens parsed, count: ' + str(len(_input_tokens)))
    logger.log_info('Classifying and filling stacks')

    # Parse tokens into stacks
    if not parser.parse_tokens(_input_tokens, _global_scope):
        logger.log_info('Stopping process')
        quit(1)
    logger.log_info('Tokens parsed')
    logger.log_info('Instructions: ' + str(_instr_stack.size()))
    logger.log_info('Data values: ' + str(_data_stack.size()))

    logger.log_info('Starting interpreting...')

    # Interpret program
    _success = interpreter.interpret_program(_global_scope, constants.BlockType.GLOBAL)

    if _success:
        logger.log_info('OK')


if __name__ == '__main__':
    main(sys.argv[1:])

logger.end_logging()

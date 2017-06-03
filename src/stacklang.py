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

from runtime import interpreter
from runtime import stackservice
from tools import logger
from tools import parser
from tools import reader

DEFAULT_FILE = 'test.txt'
PROGRAM_NAME = 'PINOTULKKI'

_file_rows = []  # input file lines
_input_tokens = []  # input tokens

_instr_stack = stackservice.create_stack('global_instr_stack')  # Instructions stack
_data_stack = stackservice.create_stack('global_data_stack')  # Data stack


# Program entry point
def main(args):
    global _file_rows
    global _input_tokens
    global _instr_stack
    global _data_stack

    input_file = ''

    if len(args) == 0:
        logger.log_info('No input file given, defaulting')
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
    parser.parse_tokens(_input_tokens, _instr_stack, _data_stack)
    logger.log_info('Tokens parsed')
    logger.log_info('Instructions: ' + str(_instr_stack.size()))
    logger.log_info('Data values: ' + str(_data_stack.size()))

    logger.log_info('Starting interpreting...')

    # Flag identifies successful run
    _success = True

    # Go through every instruction in stack and pass it to the interpreter
    while _instr_stack.size() > 0:
        instr = _instr_stack.pop()
        if interpreter.handle_command(instr, _data_stack):
            continue
        else:
            logger.log_error('Conflicting instruction: ' + instr)
            logger.log_error('Stopping interpreter')
            _success = False
            break

    if _success:
        logger.log_info('OK')


if __name__ == '__main__':
    main(sys.argv[1:])

logger.end_logging()

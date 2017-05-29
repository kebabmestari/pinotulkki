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

from tools import logger
from tools import parser
from tools import reader

from utils.stack import Stack

DEFAULTFILE = 'test.txt'
PROGRAMNAME = 'PINOTULKKI'

_file_rows = []  # input file lines
_input_tokens = []  # input tokens

_instr_stack = Stack()  # Instructions stack
_data_stack = Stack()  # Data stack


# Program entry point
def main(args):
    global _file_rows
    global _input_tokens
    global _instr_stack
    global _data_stack

    input_file = ''

    if len(args) == 0:
        logger.logWarning('No input file given')
        print('No input file given, defaulting')
        input_file = DEFAULTFILE
    else:
        input_file = args[0]

    logger.logInfo('%s started' % PROGRAMNAME)
    logger.logInfo('Input file: ' + input_file)

    try:
        _file_rows = reader.readfile(os.getcwd(), input_file)
    except FileNotFoundError:
        logger.logError('File does not exists')
        return
    except IOError:
        logger.logError('IO error while reading input file')
        return

    logger.logInfo('File read')
    logger.logInfo('Parsing tokens')

    # Break file into singular tokens
    _input_tokens = parser.break_lines(_file_rows)

    logger.logInfo('Tokens parsed, count: ' + str(len(_input_tokens)))
    logger.logInfo('Classifying and filling stacks')

    # Parse tokens into stacks
    parser.parse_tokens(_input_tokens, _instr_stack, _data_stack)
    logger.logInfo('Tokens parsed')
    logger.logInfo('Instructions: ' + str(_instr_stack.size()))
    logger.logInfo('Data values: ' + str(_data_stack.size()))

    logger.logInfo('Starting interpreting...\n\n')

    # Flag identifies successful run
    _success = True

    # Go through every instruction in stack and pass it to the interpreter
    while _instr_stack.size() > 0:
        instr = _instr_stack.pop()
        if interpreter.handle_command(instr, _data_stack):
            continue
        else:
            logger.logError('Conflicting instruction: ' + instr)
            logger.logError('Stopping interpreter')
            _success = False
            break

    if _success:
        logger.logInfo('OK')


if __name__ == '__main__':
    main(sys.argv[1:])

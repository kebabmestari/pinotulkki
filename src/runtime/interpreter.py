# Dictionary that maps language's commands to handler functions

from inspect import signature

from tools import logger

# Modules
from modules import io
from modules import stack
from modules import arithmetic
from modules import comparison
from modules import logic
from modules import graphics


# test handler pls ignore
def foo():
    print('FOO')


# SYNTAX DICTIONARY
# MAPS INSTRUCTION LITERAL TO HANDLER FUNCTION
CMD = {
    # MATH
    '+': arithmetic.plus_handler,
    '-': arithmetic.minus_handler,
    '*': arithmetic.multiply_handler,
    '/': arithmetic.division_handler,

    # LOGIC
    'and': logic.and_handler,
    'or': logic.or_handler,
    'not': logic.not_handler,

    # COMPARISON
    '<': comparison.lt_handler,
    '>': comparison.gt_handler,
    '==': comparison.eq_handler,
    '!=': comparison.neq_handler,

    # STACK
    'dup': stack.dup_handler,
    'rot': foo,
    'swap': stack.swap_handler,
    'drop': foo,
    'over': foo,
    'nip': foo,
    'tuck': foo,

    # IO
    'print': io.print_handler,
    'read': io.read_handler,
}


# Return a list of reserved instruction words
def get_instruction_words():
    return list(CMD.keys())


# Return handler function
def get_instruction_handler(cmd):
    return CMD[cmd]


# Call a corresponding function from the dictionary
# False indicates failure, True success
def handle_command(cmd, data):
    params = []
    if cmd in get_instruction_words():
        handler = get_instruction_handler(cmd)
        sig = signature(handler)
        param_count = len(sig.parameters)  # number of arguments
        for i in range(param_count):  # extract arguments from the top of data stack
            dat = data.pop()
            if dat is None:
                logger.logError('Argument error: Ran out of values in data stack')
                logger.logError('Values were: ' + str(params))
                return False
            params.append(dat)
        logger.logDebug('Interpreting instruction: ' + str(cmd) + ' with arguments ' + str(params))
        result = handler(*params)  # call handler
        if result is not None:
            if isinstance(result, list):
                data.extend(result)
            else:
                data.push(result)  # push the result into the top of the data stack
            logger.logDebug('Pushed result ' + str(result))
    else:
        logger.logError('Invalid instruction word ' + str(cmd))
    return True

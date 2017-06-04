# Dictionary that maps language's commands to handler functions
from inspect import signature

from common import constants
from modules import arithmetic, stash
from modules import comparison
from modules import graphics
# Modules
from modules import io
from modules import logic
from modules import stack
from runtime import scopeservice
from tools import converter
from tools import logger


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
    'rot': stack.rot_handler,
    'rot-': stack.rot_minus_handler,
    'roll4': stack.roll4_handler,
    'roll4-': stack.roll4_minus_handler,
    'swap': stack.swap_handler,
    'drop': stack.drop_handler,
    'over': stack.over_handler,
    'nip': stack.nip_handler,
    'tuck': stack.tuck_handler,

    # IO
    '.': io.print_handler,
    'read': io.read_handler,

    # GRAPHICS
    'gfxinit': graphics.init_handler,
    'circle': graphics.circle_handler,
    'box': graphics.box_handler,
    'rect': graphics.rect_handler,
    'line': graphics.line_handler,
    'triangle': graphics.triangle_handler,
    'color': graphics.color_handler,

    # STASH
    'push': stash.push_stash_handler,
    'pull': stash.pull_stash_handler,

}


# Return a list of reserved instruction words
def get_instruction_words():
    return list(CMD.keys())


# Return handler function
def get_instruction_handler(cmd):
    return CMD[cmd]


def interpret_program(scope, scope_type):
    # Fetch the stacks and make copies of them
    instr_stack = scopeservice.copy_instr_stack(scope['id'])
    data_stack = scopeservice.copy_data_stack(scope['id'])

    ibs = constants.IF_BLOCK_SYMBOLS
    lbs = constants.LOOP_BLOCK_SYMBOLS

    # Go through every instruction in stack and pass it to the interpreter
    while instr_stack.size() > 0:
        instr = instr_stack.pop()

        # Handle control instructions
        if instr[0] == ibs[0]:  # if block
            logger.log_debug('Interpreting control instruction IF')
            if not data_stack.pop():  # do not proceed into scope if previous value is False
                logger.log_debug('Evaluated False, not proceeding to block')
                continue
            ref = parse_scope_symbol_ref(instr)
            scope_type = constants.BlockType.IF
            newscope = scopeservice.get_scope(ref)
            logger.log_debug('Evaluated True, proceeding to block ' + newscope['name'] + ' ' + str(newscope['id']))
            if not interpret_program(newscope, scope_type):
                return False
            continue

        # Handle control instructions
        if instr[0] == lbs[0]:  # loop block
            ref = parse_scope_symbol_ref(instr)
            scope_type = constants.BlockType.LOOP
            newscope = scopeservice.get_scope(ref)
            logger.log_debug('Entering loop block ' + newscope['name'] + ' ' + str(newscope['id']))
            while interpret_program(newscope, scope_type):
                logger.log_debug('Looping block ' + newscope['name'] + ' ' + str(newscope['id']))
                pass
            continue

        if handle_command(instr, data_stack):
            continue
        else:
            logger.log_error('Conflicting instruction: ' + instr)
            logger.log_error('Stopping interpreter')
            return False

    if scope_type == constants.BlockType.LOOP:
        loop_condition = data_stack.pop()
        if not loop_condition:
            logger.log_debug('Exiting loop block ' + scope['name'] + ' ' + str(scope['id']))
        return bool(loop_condition)

    logger.log_debug('Leaving scope ' + scope['name'] + ' ' + str(scope['id']))

    return True


def parse_scope_symbol_ref(token):
    return int(token[1:])


# Call a corresponding function from the dictionary
# False indicates failure, True success
def handle_command(cmd, data):
    params = []
    if cmd in get_instruction_words():

        logger.log_debug('STACK: ' + str(data))

        handler = get_instruction_handler(cmd)
        sig = signature(handler)
        param_count = len(sig.parameters)  # number of arguments

        for i in range(param_count):  # extract arguments from the top of data stack
            dat = data.pop()
            if dat is None:
                logger.log_error('Argument error: Ran out of values in data stack')
                logger.log_error('Values were: ' + str(params))
                return False
            params.append(dat)

        logger.log_debug('Interpreting instruction: ' + str(cmd) + ' with arguments ' + str(params))

        try:
            result = handler(*params)  # call handler
        except ValueError:
            logger.log_error('Invalid types of arguments')
            return False

        if cmd in constants.PLACEHOLDER_FUNCTIONS:
            if isinstance(result, str):
                result = converter.convert_token(result)  # convert user inputted string
            # Replace next placeholder with returned value
            if not data.replace_placeholder(constants.PLACEHOLDER_SYMBOL, result):
                logger.log_error('No expected placeholder value')
                return False
        elif result is not None:
            data.push_front(result)  # push the result into the top of the data stack
            logger.log_debug('Pushed result ' + str(result))
        elif cmd in constants.NO_POP_FUNCTIONS:
            # Handler should not remove the data from stack -> return to stack
            # For example, print function should not remove values from stack
            data.push_front(params)
    else:
        logger.log_error('Invalid instruction word ' + str(cmd))
    return True

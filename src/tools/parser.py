from common import constants
from common.constants import BlockType
from runtime import scopeservice
from runtime.interpreter import get_instruction_words
from tools import converter
from tools import logger

INSTRUCTIONS = get_instruction_words()


# Break down lines into continuous list of tokens
def break_lines(lines, delimiter=constants.DEFAULT_DELIMITER):
    result = []
    for line in lines:
        line = str(line)
        result.extend(line.split(delimiter))
    return result


def parse_tokens(tokens, start_scope):
    target_scope = scopeservice.get_scope(start_scope['id'])  # get global scope
    instr = scopeservice.get_instr_stack(start_scope['id'])
    data = scopeservice.get_data_stack(start_scope['id'])

    block_open_count = 0

    for token in tokens:

        # Token is an instruction
        if token in INSTRUCTIONS:
            if token in constants.PLACEHOLDER_FUNCTIONS:
                # Token is an instruction that needs a placeholder value in stack
                data.push(constants.PLACEHOLDER_SYMBOL)
                logger.log_debug('DAT: PLACEHOLDER ' + constants.COMMENT_SYMBOL)
            instr.push(token)
            logger.log_debug('INSTR ' + str(instr.size()) + ': ' + token)

        # Token is a block opening symbol
        elif token == constants.IF_BLOCK_SYMBOLS[0] or token == constants.LOOP_BLOCK_SYMBOLS[0]:
            # get scope type values
            block_type = BlockType.IF if token == constants.IF_BLOCK_SYMBOLS[0] else BlockType.LOOP
            block_name = 'if' if block_type == BlockType.IF else 'loop'
            block_symbol = constants.IF_BLOCK_SYMBOLS[0] if block_type == BlockType.IF else \
            constants.LOOP_BLOCK_SYMBOLS[0]
            # symbol begins a new block
            block_open_count += 1
            # create new local scope
            new_scope = scopeservice.create_scope(block_name + '_scope', target_scope['id'])
            # insert reference to the current scope
            instr.push(block_symbol + str(new_scope['id']))
            # switch the target scope to the newly created
            target_scope = new_scope
            instr = scopeservice.get_instr_stack(target_scope['id'])
            data = scopeservice.get_data_stack(target_scope['id'])
            logger.log_debug('SCOPEOPEN: ' + str(new_scope['id']))

        # Token is a block closing symbol
        elif token == constants.IF_BLOCK_SYMBOLS[1] or token == constants.LOOP_BLOCK_SYMBOLS[1]:
            # symbol closes a block
            block_open_count -= 1
            # get the upper scope
            parent_scope = scopeservice.get_scope(target_scope['parent'])
            # switch the target scope to the newly created
            logger.log_debug('SCOPECLOSE: ' + str(target_scope['id']))
            if parent_scope['id'] < 0:
                logger.log_error('Number of scopes do not match, check your opening and closing symbols')
                return False
            target_scope = parent_scope
            instr = scopeservice.get_instr_stack(target_scope['id'])
            data = scopeservice.get_data_stack(target_scope['id'])


        # Token is a data value
        else:
            token = converter.convert_token(token)
            logger.log_debug('DAT: ' + str(token))
            data.push(token)

    if block_open_count > 0:
        logger.log_error('Block not closed before the end of file')
        return False

    return True

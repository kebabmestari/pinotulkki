from runtime.interpreter import get_instruction_words
from tools import logger
from tools import converter
from common import constants

INSTRUCTIONS = get_instruction_words()


# Break down lines into continuous list of tokens
def break_lines(lines, delimiter=constants.DEFAULT_DELIMITER):
    result = []
    for line in lines:
        line = str(line)
        result.extend(line.split(delimiter))
    return result


def parse_tokens(tokens, instr, data):
    for token in tokens:

        # Token is an instruction, else it's a data value
        if token in INSTRUCTIONS:
            if token in constants.PLACEHOLDER_FUNCTIONS:
                # Token is an instruction that needs a placeholder value in stack
                data.push(constants.PLACEHOLDER_SYMBOL)
                logger.log_debug('DAT: PLACEHOLDER ' + constants.COMMENT_SYMBOL)
            instr.push(token)
            logger.log_debug('INSTR ' + str(instr.size()) + ': ' + token)
        else:
            token = converter.convert_token(token)
            logger.log_debug('DAT: ' + str(token))
            data.push(token)

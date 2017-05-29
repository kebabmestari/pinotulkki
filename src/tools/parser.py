from utils import stack
from tools import logger
from numbers import Integral
from runtime.interpreter import get_instruction_words

INSTRUCTIONS = get_instruction_words()


# Break down lines into continuous list of tokens
def break_lines(lines, delimiter=' '):
    result = []
    for line in lines:
        line = str(line)
        result.extend(line.split(delimiter))
    return result


def parse_tokens(tokens, instr, data):
    for token in tokens:
        # Token is an instruction, else it's a data value
        if token in INSTRUCTIONS:
            instr.push(token)
            logger.logDebug('INSTR ' + str(instr.size()) + ': ' + token)
        else:
            if token.isdigit():
                token = int(token)
                data.push(token)
                logger.logDebug('DATA ' + str(data.size()) + ' INT: ' + str(token))
            else:
                token = str(token)
                if token == 'true' or token == 'false':
                    # Boolean value
                    if token == 'true':
                        data.push(True)
                    elif token == 'false':
                        data.push(False)
                    logger.logDebug('DATA ' + str(data.size()) + ' BOOL: ' + token)
                else:
                    # String value
                    data.push(token)
                    logger.logDebug('DATA ' + str(data.size()) + ' STR: ' + token)

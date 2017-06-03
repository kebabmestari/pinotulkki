# list to hold lists each of which represents
# a sub instruction
from common.inversestack import InverseStack
from tools import logger

_next_stack_id = 0
_stack_list = []


def create_stack(name = ''):
    global _next_stack_id
    result = InverseStack(_next_stack_id, name)
    _stack_list.append(result)
    _next_stack_id += 1
    return result


def get_instr_stack(id):
    global _stack_list
    if id < 0 or id >= len(_stack_list):
        logger.log_error('Queried stack which does not exists')
        return None
    return _stack_list[id]

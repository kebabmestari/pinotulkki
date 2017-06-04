# list to hold lists each of which represents
# a sub instruction
import copy

from common.inversestack import InverseStack
from tools import logger

_next_scope_id = 0
_scope_dict = []


def create_scope(name='', parent_scope=0):
    global _next_scope_id
    _scope_dict.append({
        'instr': InverseStack(),
        'data': InverseStack(),
        'name': name,
        'parent': parent_scope,
        'id': _next_scope_id
    })
    if name != '':
        logger.log_debug('Scope ' + name + ' ID ' + str(_next_scope_id) + ' created')
    else:
        logger.log_debug('Scope ID ' + str(_next_scope_id) + ' created')
    _next_scope_id += 1
    return get_scope(_next_scope_id - 1)


def get_scope(id):
    global _scope_dict
    if id < 0 or id >= len(_scope_dict):
        logger.log_error('Queried scope ' + id + ' which does not exists')
        return None
    return _scope_dict[id]


def get_instr_stack(id):
    scope = get_scope(id)
    if scope:
        return scope['instr']
    else:
        return None


def copy_instr_stack(id):
    scope = get_scope(id)
    if scope:
        return copy.deepcopy(scope['instr'])
    else:
        return None


def get_data_stack(id):
    scope = get_scope(id)
    if scope:
        return scope['data']
    else:
        return None


def copy_data_stack(id):
    scope = get_scope(id)
    if scope:
        return copy.deepcopy(scope['data'])
    else:
        return None


def get_parent_scope(id):
    scope = get_scope(id)
    if scope:
        return scope['parent']
    else:
        return None


def _debug_print_scopes():
    for s in _scope_dict:
        logger.log_debug('SCOPE: ' + str(s['id']) + " " + s['name'])
        logger.log_debug('INSTR: ' + str(s['instr']))
        logger.log_debug('DATA: ' + str(s['data']))

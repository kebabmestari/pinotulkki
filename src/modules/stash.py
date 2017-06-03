from tools import logger

_global_stash = dict()

def push_stash_handler(value, name):
    _global_stash[name] = value

def pull_stash_handler(name):
    try:
        result = _global_stash[name]
    except KeyError:
        logger.log_error('Invalid stash key ' + name)
        return None
    return result

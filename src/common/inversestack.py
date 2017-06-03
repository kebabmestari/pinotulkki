'''
    Class implements inverse stack
    Global stack is always id 0
'''
from tools import logger

class InverseStack:
    def __init__(self, id, name=''):
        self.items = []
        self.id = id
        self.name = name
        if name == '':
            logger.log_debug('Stack id ' + str(id) + ' created')
        else:
            logger.log_debug('Stack ' + self.name + ' id ' + str(id) + ' created')

    def push(self, item):
        self.items.append(item)

    def push_front(self, item):
        if isinstance(item, list):
            for i in item:
                self.push_front(i)
        else:
            self.items.insert(0, item)

    def peek(self):
        return self.items[0]

    def pop(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def get_id(self):
        return self.id

    def replace_placeholder(self, symbol, value):
        for i in range(len(self.items)):
            if self.items[i] == symbol:
                self.items[i] = value;
                return True
        return False

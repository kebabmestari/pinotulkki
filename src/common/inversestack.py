'''
    Class implements stack
    Small abstraction over list
'''


class InverseStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def push_front(self, item):
        if isinstance(item, list):
            for i in item:
                self.push_front(i)
        else:
            self.items.insert(0, item)

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
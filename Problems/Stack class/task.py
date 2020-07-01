class Stack():

    def __init__(self):
        self.table = []
        self.el = None

    def push(self, el):
        self.table.append(el)

    def pop(self):
        return self.table.pop()

    def peek(self):
        return self.table[-1]

    def is_empty(self):
        return len(self.table) == 0

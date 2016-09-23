from stack import Stack


class UpgradedStack(Stack):
    def __init__(self):
        super(Stack, self).__init__()
        self.items = []
        self.__max_stack = Stack()

    def max_val(self):
        # return self.__max_stack.peek()
        pass

    def push(self, item):
        pass

    def pop(self):
        pass

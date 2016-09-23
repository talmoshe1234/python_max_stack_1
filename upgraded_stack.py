from stack import Stack


class UpgradedStack(Stack):
    def __init__(self):
        super(Stack, self).__init__()
        self.items = []
        self.__max_stack = Stack()

    def max_val(self):
        return  self.__max_stack.peek()

    def push(self, item):
        if self.__max_stack.is_empty():
            self.__max_stack.push(item)
            super(UpgradedStack, self).push(item)
        elif self.__max_stack.peek() < item:
            self.__max_stack.push(item)
            super(UpgradedStack, self).push(item)
        else:
            super(UpgradedStack, self).push(item)


    def pop(self):

        if super(UpgradedStack, self).is_empty()==False:
           a = super(UpgradedStack, self).pop()
           if a == self.__max_stack.peek():
               return self.__max_stack.pop()
           else:
               return a



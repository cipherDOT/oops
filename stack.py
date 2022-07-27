import copy

class StackOverflowError(Exception):
    pass

class StackUnderflowError(Exception):
    pass

class QueueOverflowError(Exception):
    pass

class QueueUnderflowError(Exception):
    pass

class Node(object):
    """
    Node simply holds a value.\n
    Node has a default value of None.\n
    """
    def __init__(self, value = None):
        self.value = value

    def null(self):
        self.value = None

    def set_val(self, val):
        self.value = val

class Stack(object):
    """
    A Stack -> object, has a initial value to set its length.\n
    It you push when a stack is full, it raises StackOverflowError.\n
    If you pop when a stack is empty, it raises StackUnderflowError.
    """
    def __init__(self, stack_length: int) -> None:
        self.l = stack_length
        self.nodes = [Node() for _ in range(self.l)]

    def push(self, val):
        overflow_checker = 0
        for n in self.nodes:
            if n.value == None:
                n.set_val(val)
                break
            else:
                overflow_checker += 1

        if overflow_checker == len(self.nodes):
            raise StackOverflowError

    def pop(self):
        underflow_checker = len(self.nodes)
        for n in self.nodes[::-1]:
            if n.value != None:
                temp = n.value
                n.null()
                return temp
            else:
                underflow_checker -= 1

        if underflow_checker == 0:
            raise StackUnderflowError

    def disp(self):
        print([n.value for n in self.nodes])



class Queue(object):
    """
    A Stack -> object, has a initial value to set its length.\n
    It you push when a stack is full, it raises StackOverflowError.\n
    If you pop when a stack is empty, it raises StackUnderflowError.
    """
    def __init__(self, stack_length: int) -> None:
        self.l = stack_length
        self.nodes = [Node() for _ in range(self.l)]

    def push(self, val):
        overflow_checker = 0
        for n in self.nodes:
            if n.value == None:
                n.set_val(val)
                break
            else:
                overflow_checker += 1

        if overflow_checker >= len(self.nodes):
            raise QueueOverflowError

    def pop(self):
        underflow_checker = 0
        for n in self.nodes:
            if n.value != None:
                duplicate = copy.copy(self.nodes[::-1])
                temp = duplicate.pop()
                self.nodes = copy.copy(duplicate[::-1]) + [Node()]
                return temp.value
            else:
                underflow_checker += 1

        if underflow_checker > len(self.nodes):
            raise QueueUnderflowError

    def disp(self):
        print([n.value for n in self.nodes])

# string reversal program
name = "Kavin"
s = Stack(len(name))

for i in name:
    s.push(i)

for i in range(len(name)):
    print(s.pop(), end = "")

print()
s.disp()

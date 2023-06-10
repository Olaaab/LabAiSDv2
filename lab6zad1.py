class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stos jest pusty")
        return self.stack.pop()

    def top(self):
        if self.is_empty():
            raise IndexError("Stos jest pusty")
        return self.stack[-1]


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.top())
print(stack.pop())
print(stack.size())
print(stack.is_empty())

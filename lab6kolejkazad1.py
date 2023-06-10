class Queue:
    def __init__(self):
        self.queue = []
        self.head = 0
        self.tail = 0

    def enqueue(self, item):
        self.queue.append(item)
        self.tail += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Kolejka jest pusta")
        item = self.queue[self.head]
        self.head += 1
        if self.head == self.tail:
            self.head = 0
            self.tail = 0
        return item

    def isEmpty(self):
        return self.head == self.tail

    def size(self):
        return self.tail - self.head


q = Queue()
print(q.isEmpty())

q.enqueue(5)
q.enqueue('kot')
q.enqueue(True)

print(q.size())
print(q.isEmpty())

q.enqueue(8.4)

print(q.dequeue())
print(q.dequeue())

print(q.size())

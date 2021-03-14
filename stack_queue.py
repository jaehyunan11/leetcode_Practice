from collections import deque

# Last in First Out (LIFO)


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


pq = Queue()
pq.enqueue({
    'company': 'wal mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({
    'company': 'wal mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
# print(pq.size())

# q = deque()
# q.appendleft(5)
# q.appendleft(8)
# q.appendleft(27)
# print(q)
# q.pop()
# print(q)

# s = Stack()
# s.push(5)
# print(s.peek())
# s.pop()
# print(s.is_empty())


fruits = []

fruits.append('banana')
fruits.append('grapes')
fruits.append('mango')
fruits.append('orange')
print(fruits)

# dequeue our fruites, we should get 'banana'
first_item = fruits.pop(0)
print(first_item)

first_item = fruits.pop(0)
print(first_item)


print(fruits)

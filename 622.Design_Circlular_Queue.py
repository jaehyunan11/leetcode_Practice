class MycircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.queue = []

    def enQueue(self, value: int):
        # insert an element into the circular queue. Return true if the operation is successful.
        if self.isFull():
            return False
        self.queue.insert(0, value)
        return True

    def deQueue(self):
        if self.queue:
            self.queue.pop()
            return True
        else:
            return False

    def Front(self):
        # Get the front item from the queue
        if self.queue:
            return self.queue[-1]
        else:
            return -1

    def Rear(self):
        if self.queue:
            return self.queue[0]
        else:
            return -1

    def isEmpty(self):
        if len(self.queue) > 0:
            return False
        else:
            return True

    def isFull(self):
        if len(self.queue) >= self.capacity:
            return True
        else:
            return False

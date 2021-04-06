class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.queue = []

    def next(self, val):
        if len(self.queue) == self.size:
            self.queue.pop(0)
        self.queue.append(val)
        return sum(self.queue) / len(self.queue)

# TIME and Space : O(N) since we traverse the num in queue and is quired to have extra space for queue.

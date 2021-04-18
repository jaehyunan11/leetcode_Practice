from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict

    def get(self, key):
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            # update in the front and remove last item
            self.cache.popitem(last=False)
        self.cache[key] = value

# TIME : O(1) both for put and get since all operations with ordered dictionary :
# SPACE : O(Capacity) since the space is used only for an ordered dictionary with at most capacity + 1 elements.

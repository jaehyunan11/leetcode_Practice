# from collections import OrderedDict


# class Node:
#     def __init__(self, key, val):
#         self.key = key
#         self.val = val
#         self.prev = None
#         self.next = None


# class LRUCache:

#     def __init__(self, Capacity):
#         self.capacity = Capacity
#         self.cache = OrderedDict()

#     def get(self, key):
#         if key not in self.cache:
#             return -1
#         val = self.cache[key]
#         self.cache.move_to_end(key)
#         return val

#     def put(self, key, val):
#         if key in self.cache:
#             del self.cache[key]
#         self.cache[key] = val
#         # If self.cache is exceed capacity, remove
#         if len(self.cache) > self.capacity:
#             self.cache.popitem(last=False)

from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

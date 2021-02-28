import random


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here
        """
        self.dict = {}  # dictionary or hashmap
        self.arr = []  # Array

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        self.arr.append(val)
        # set index value
        self.dict[val] = len(self.arr) - 1
        print(self.arr)
        print(self.dict)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        # val not available the dictionary
        if val not in self.dict:
            return False
        # set index value in dictionary
        idx = self.dict[val]
        # Last Value in the array
        last_val = self.arr[-1]
        # swap the last_val index to val index
        self.dict[last_val] = idx
        # Swap last val and index
        self.arr[-1], self.arr[idx] = self.arr[idx], self.arr[-1]
        # delete the last vale in the arr which is val
        self.arr.pop()
        # delete val in the dict
        del self.dict[val]
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        """
        return random.choice(self.arr)


R = RandomizedSet()
print(R.insert(1))
print(R.insert(2))
print(R.insert(3))
print(R.remove(2))
print(R.getRandom())

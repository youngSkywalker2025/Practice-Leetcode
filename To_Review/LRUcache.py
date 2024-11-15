from collections import OrderedDict
'''Ordered Dict internally implements a doubly linked list to maintain the order of items'''
'''To implement the LRU cache, a combination of a hashmap and a doubly linked list is used'''


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move key to end to mark it as recently used
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove the old value to update
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            # Remove the least recently used item
            self.cache.popitem(last=False)
        self.cache[key] = value

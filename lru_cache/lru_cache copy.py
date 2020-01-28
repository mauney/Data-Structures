import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.dll = DoublyLinkedList()
        self.dict= dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.dict:
            self.dll.move_to_front(self.dict[key])
            return self.dict[key].value
        else:
            return None



    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key not in self.dict:
            if self.size >= self.limit:
                # decrement size
                self.size -= 1
                # remove dll tail from dict
                for tail_key, tail_value in self.dict:
                    if tail_value == value:
                        self.dict.pop([tail_key])
                # remove tail from dll
                self.dll.remove_from_tail()
            # increment size
            self.size += 1
            # insert item at head of dll
            self.dll.add_to_head(self.dict[key])
            # add item to dict
            self.dict[key] = self.dll.head
        else:
            # update value
            self.dict[key].value = value
            # move item to head of dll
            self.dll.move_to_front(self.dict[key])


cache = LRUCache(3)
print(cache.size, cache.limit, cache.dict, cache.dll)
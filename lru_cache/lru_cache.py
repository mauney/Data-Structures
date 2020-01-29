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
        self.queue = DoublyLinkedList()
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:
            self.queue.move_to_front(self.storage[key])
            return self.storage[key].value[1]
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
        if key not in self.storage:
            if self.queue.length >= self.limit:
                # remove queue tail from storage
                del self.storage[self.queue.tail.value[0]]
                # remove tail from queue
                self.queue.remove_from_tail()
            # insert item at head of queue
            self.queue.add_to_head((key, value))
            # add item to storage
            self.storage[key] = self.queue.head
        else:
            # update node value if key already exists
            self.storage[key].value = (key, value)
            # move item to head of queue
            self.queue.move_to_front(self.storage[key])

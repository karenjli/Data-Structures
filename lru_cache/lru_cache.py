
from doubly_linked_list import ListNode, DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self,  limit=10):
        self.limit = limit
        self.size = 0
        self.order = DoublyLinkedList()
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # Is key in cache?
        if key in self.storage:
            # node equals the value of the key
            node = self.storage[key]
            # Add the key-value pair to the head of the list
            self.order.move_to_end(node)
            # Return the first value of the list
            return node.value[1]
        else:
            # Return none if key doesn't exist
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
        # Check if key is already there
        # if key in self.cache.keys():
        #     # If yes, identify the node
        #     node = self.cache[key]
        #     node.value = (key, value)
        #     self.list.move_to_front(node)
        #     return self.list.head
        # else:
        #     if self.size == self.limit:
        #         del self.cache[self.list.remove_from_tail()[0]]
        #         self.size -= 1

        #     new_cache = (key, value)
        #     self.list.add_to_head(new_cache)
        #     self.cache[key] = self.list.head
        #     self.size += 1

        # Create a node if key not found and move to front
        # Move node to front if key found
        # If full remove last node from linked list and dictionary

        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_end(node)
            return

        if self.size == self.limit:
            del self.storage[self.order.head.value[0]]
            self.order.remove_from_head()
            self.size -= 1

        # add to the end of the list
        self.order.add_to_tail((key, value))
        # set the cache
        self.storage[key] = self.order.tail
        self.size += 1

# make a node class for doubly linked list

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    # initialize with cache, capacity, dummy nodes left and right, then link them together doubly linked
    def __init__(self, capacity):
        self.cache = {}  # key : node
        self.cap = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # remove any node
    # O -> 1 -> 2
    #   <-   <-
    # O -> 2
    #   <-
    def remove(self, node):
        nxt = node.next
        previous = node.prev

        previous.next = nxt
        nxt.prev = previous
    # insert at the right
    # 0 -> 2
    #   <-
    # 0 -> 1 -> 2
    #   <-   <-
    def insert(self, node):
        previous = self.right.prev
        nxt = self.right

        previous.next = node
        node.next = nxt
        nxt.prev = node
        node.prev = previous

    # return value of key if key exists
    # if key exists, (update and return value since you are using it) remove and insert at the right to show most recently used
    # else return -1
    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    # update value of key if exists
    # if key in cache, remove it from cache, replace spot in cache with separate node for it and insert that into the doubly linked list
    # check if number of keys is more than capacity, the LRU is the left.next since left is a dummy, then delete the lru node with the lru key
    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# left and right nodes
# left = least recently used
# right = most recently used
# doubly linked list, hashmap

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key : node
        # initialized as dummies
        self.left = Node(0, 0)  # least recently used node
        self.right = Node(0, 0)  # most recently used node
        # .next and .prev are the real values
        self.left.next = self.right  # link them together
        self.right.prev = self.left

    # remove node from list doubly linked list
    def remove(self, node):
        nxt = node.next
        previous = node.prev

        previous.next = nxt
        nxt.prev = previous

    # insert node at right
    def insert(self, node):
        previous = self.right.prev
        nxt = self.right

        previous.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = previous

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])  # remove and insert at the right to show
            self.insert(self.cache[key])  # most recently used node
            return self.cache[key].val  # self.cache[key] returns node, .val returns real val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:  # node already exists in list with same key/val
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:  # remove from list and delete LRU from hashmap
            lru = self.left.next  # always LRU
            self.remove(lru)
            del self.cache[lru.key]

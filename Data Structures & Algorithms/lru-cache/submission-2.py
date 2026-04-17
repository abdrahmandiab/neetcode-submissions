class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left


    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self,node):
        prev =  self.right.prev
        nxt = self.right
        prev.next = nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key):
            #remove the old link
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.cap:
            lru = self.left.next
            self.remove(lru)
            self.cache.pop(lru.key)
        
# Dict will look like
# {
#  1: pointer to Node(1,1)
#  2: pointer to Node(2,2)
# }

# on get:
# we want to get the val
# we want to update the MRU
# What do we do if right becomes = to left?

# on put:
# we want to add the key_val to the kv_store as key:new_node
# we want to set the MRU to new_node
# we want to set LRU = LRU.next
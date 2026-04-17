"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}
        cur = head
        dup = iterator = new_cur = Node(0)
        while cur:
            new_cur.next = Node(cur.val)
            new_cur = new_cur.next
            old_to_new[cur] = new_cur
            new_cur.random = cur.random
            cur = cur.next
        print(old_to_new)
        #now correct references using old_to_new[old_ref from the new heads]
        iterator = iterator.next
        while iterator:
            if iterator.random:
                iterator.random = old_to_new[iterator.random]
            iterator = iterator.next
        return dup.next
            

# head_map has: new pointer to old pointer
# OR old pointer to new pointer
# OR old pointer to old pointer.

# The issue is, we don't have the memory location of the new 
#   Nodes during creation
# So, we need to store for each Node, where it previously used to go to.
# We also need to store for each Node, what its new reference is.
# On second pass, we old_to_new[[check used_to_go[node_1]]
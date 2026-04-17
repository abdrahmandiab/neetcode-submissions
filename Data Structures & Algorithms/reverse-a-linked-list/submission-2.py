# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev



# [1]->[2]->[3]->None

# insert None as prev
#   None ->  [1] ->[2]->[3]->None
# prev^   curr^

# we say,
# tmp = curr.next ([2])
# curr.next = prev
# prev = curr
# curr = tmp

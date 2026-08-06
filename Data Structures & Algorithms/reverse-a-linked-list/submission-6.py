# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        return prev


# None -> a -> b -> c
# end with
# None -> c -> b -> a
# so I must do:
# a <- b -> c

# if a is cur
# prev is None
# b is cur.next
# we want a to point to None.
# so cur.next = prev
# but then we would lose the b
# so we store tmp = cur.next

# at final step
# we have cur == c -> None, prev = b
# we set #  tmp = cur.next | tmp = None
         #    cur.next = prev | c -> b
         #    prev = cur | prev = c
         #    cur = tmp | cur = None
         # So we return c, which is prev

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dup = new = ListNode(0)
        carry_over = 0
        while (l1 or l2) or (carry_over !=0):
            dup.next = ListNode(0)
            dup = dup.next
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            dup.val = (l1_val + l2_val + carry_over) % 10
            carry_over = (l1_val + l2_val + carry_over) //10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return new.next
class DLL:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next # pointer to next element
        self.prev = prev # pointer to previous element


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        head = DLL(tokens[0])
        curr = head
        for i in range(1,len(tokens)):
            curr.next = DLL(tokens[i],prev=curr)
            curr = curr.next
        ans = -1
        while head is not None:
            if head.val in "+-*/":
                l = int(head.prev.prev.val)
                r = int(head.prev.val)
                if head.val == '+':
                    res = l + r
                elif head.val == '-':
                    res = l - r
                elif head.val == '*':
                    res = l * r
                else:
                    res = int(l / r)
                head.val = str(res)
                head.prev = head.prev.prev.prev
                if head.prev is not None:
                    head.prev.next = head
            ans = int(head.val)
            head = head.next
        return ans


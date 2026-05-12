# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif (p and not q) or (q and not p):
            return False
        if p.val == q.val:
            if (p.left and not q.left) or (q.left and not p.left):
                return False
            if (p.right and not q.right) or (q.right and not p.right):
                return False
            
            if (p.left and q.left):
                if not self.isSameTree(p.left, q.left):
                    return False
            if (p.right and q.right):
                if not self.isSameTree(p.right,q.right):
                    return False
            return  True 
        else:
            return False
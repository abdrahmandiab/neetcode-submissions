# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        roots = []
        if root:
            roots = [root]
        while roots:
            roots_in = roots
            roots = []
            acc = []
            for r in roots_in:
                acc.append(r.val)
                if r.left:
                    roots.append(r.left)
                if r.right:
                    roots.append(r.right)
            ret.append(acc)
        return ret
        

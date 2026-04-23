# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res,left+right)
            return 1+max(left,right)
        dfs(root)
        return res
        



# We find the deepest branch on left, and right, and compare their depth in comparison to the current root.


#   1
#   | \
#   2  7
#   | \
#   3  6
#  / \  
# 4   5  

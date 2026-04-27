# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            if left == -1:
                return -1

            right = dfs(node.right)
            if right == -1:
                return -1
            if abs(left-right) > 1:
                return -1
            return 1 + max(dfs(node.left), dfs(node.right))
            


        return dfs(root) != -1

   
# This question is whether the tree height is balanced at every node.
# This means, Breadth and Depth in the number of nodes we need to check
# Breadth and Depth might matter in which one yields a failure first though.
# In this case, Depth is the one that will allow us to return early
# We should check at every node: Max_height left, and Max_height right, then compare the two.

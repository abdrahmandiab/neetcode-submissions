# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return (True, 0)

            left = dfs(root.left)
            right = dfs(root.right)
            height = 1 + max(left[1], right[1])
            if not left[0] or not right[0] or abs(left[1] - right[1]) > 1:
                return (False, height)
            return (True, height)

        return dfs(root)[0]

   
# This question is whether the tree height is balanced at every node.
# This means, Breadth and Depth in the number of nodes we need to check
# Breadth and Depth might matter in which one yields a failure first though.
# In this case, Depth is the one that will allow us to return early
# We should check at every node: Max_height left, and Max_height right, then compare the two.

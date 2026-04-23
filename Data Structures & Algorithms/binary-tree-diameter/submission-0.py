# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # Get diameter considering this root as pivot
        max_depth_l = self.maxHeight(root.left)
        max_depth_r = self.maxHeight(root.right)
        diameter = max_depth_l + max_depth_r
        
        # return max of this pivot or other pivots
        return max(diameter, self.diameterOfBinaryTree(root.right),self.diameterOfBinaryTree(root.left))

    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+max(self.maxHeight(root.left), self.maxHeight(root.right))
        



# We find the deepest branch on left, and right, and compare their depth in comparison to the current root.


#   1
#   | \
#   2  7
#   | \
#   3  6
#  / \  
# 4   5  

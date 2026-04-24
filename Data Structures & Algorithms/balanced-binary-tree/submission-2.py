# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        diff = left_height - right_height

        is_balanced_l = self.isBalanced(root.left)
        is_balanced_r = self.isBalanced(root.right)
        if abs(diff) <= 1 and is_balanced_l and is_balanced_r:
            return True

        return False

    def getHeight(self, node):
        if not node:
            return 0
        else:
            return 1 + max(self.getHeight(node.left),self.getHeight(node.right))
        
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            tmp_r = root.right
            tmp_l = root.left
            root.right = self.invertTree(tmp_l)
            root.left = self.invertTree(tmp_r)
        return root
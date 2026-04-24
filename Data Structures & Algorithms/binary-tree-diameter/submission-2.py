# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter is the longest path between any two nodes.
        # We need to consider paths with different nodes as the pivot point
        # We must calculate left subtree height + right subtree height for each pivot point
        # While doing a DFS to compute heights, we can simultaneously track the maximum left+right seen so far
        self.result = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            self.result = max(self.result, left + right)

            return 1 + max(left,right)
        dfs(root)
        return self.result
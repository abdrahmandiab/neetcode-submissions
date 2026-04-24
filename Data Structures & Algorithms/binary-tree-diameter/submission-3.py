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

        def dfs(node):
            if not node:
                return 0, 0
            left_height, left_diameter = dfs(node.left)
            right_height, right_diameter = dfs(node.right)

            height = 1 + max(left_height,right_height)
            diameter =  max(left_height+right_height, left_diameter, right_diameter)

            return height, diameter 
        
        return dfs(root)[1]
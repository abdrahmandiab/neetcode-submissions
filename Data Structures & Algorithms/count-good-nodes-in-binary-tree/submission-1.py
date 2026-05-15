# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num_good = [0]

        def dfs(node, max_prev_levels):
            if not node:
                return
            if node.val >= max_prev_levels:
                num_good[0]+=1
            dfs(node.left, max(max_prev_levels, node.val))
            dfs(node.right, max(max_prev_levels, node.val))
        
        dfs(root, -999)
        return num_good[0]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-infinity")
        def dfs(root):
            if not root:
                return
            left = self.maxPathSumSub(root.left)
            right = self.maxPathSumSub(root.right)
            self.res = max(self.res, left + root.val + right)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.res
    
    def maxPathSumSub(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        val = root.val
        RSub = self.maxPathSumSub(root.right)
        LSub = self.maxPathSumSub(root.left)
        path = val + max(LSub, RSub)
        return max(0,path)






# At every node, we have an option, to append to the list the [left+top, left, right + top, right, left+right].

# Hmm, there are 2 ways to do this
# Two Pass DFS: For every node to consider the top, it needs to not only know the top, 
#   but also know the sum achievable by connecting to the top.
#   We also need to know the total achievable sum from the right

# The final result is the maximum combination of 1-3 cells.
# maxPathSum = max( self.val,
#                   self.val + self.parent.val + self.left.val,
#                   self.val + self.parent.val + self.right.val,
#                   self.val + self.parent.val # Akshuallyyyy, this is redundant, because we already compute it at the parent.
#                   self.val + self.left.val
#                   self.val + self.right.val

# Maybe we go from bottom to top, (2n), accumulate the result of the best path achievable Left, and Right
# report that result to top

# Maybe 



# Greedy: For every node, just consider the top, left, and right nodes, and which adds more value
#    Cons -> Could get a situation likeeee [5 -R-> -10 -L> 99999].
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap: List[int] = []
        ret = 0
        def dfs(node):
            if not node :
                return
            heapq.heappush(heap, node.val)
            dfs(node.right)
            dfs(node.left)
        dfs(root)
        for i in range(k):
            ret = heapq.heappop(heap)
        return ret
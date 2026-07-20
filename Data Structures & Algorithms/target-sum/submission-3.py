class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = defaultdict(int)

        def dfs(i, total):
            if (i==n):
                return 1 if (total == target) else 0
            dp[(i,total)] = dfs(i+1, total+nums[i]) + dfs(i+1, total-nums[i]) 
            return dp[(i,total)]
        
        return dfs(0,0)
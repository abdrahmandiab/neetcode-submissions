class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[1],nums[0])
        for i in range(2,n,1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]





# Maximum amount of money, can't take adjacent houses.
# So this could be a situation where:
# 1. Skip middle: A (B C) D
# 2. Alternate: A (B) C (D)

# DP -> we want to save the MAXIMAL values previously calculated for a path.
#      When calculating path for next house i, consider the max of the two previous paths + the current nums[i]
#      
#      Effectively, after we have calculated dp[i-1], and dp[i-2], we can forget dp[i-3]
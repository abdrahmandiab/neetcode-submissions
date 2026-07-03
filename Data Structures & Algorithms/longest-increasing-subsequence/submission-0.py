class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        # length of the longest strictly increasing 
        # subsequence whose last element is nums[i]
        for i in range(n):
            coeff = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)

# Working through an example:
# [9,1,4,2,3,3,7]
# consider:
#  [9]
#. [1, 4, 7]
#  [1, 2, 3, 7]
#. [4, 7]
#. [2, 3 , 7]
#  [3, 7] x2
#  [7]

# So, we can say:
#.  dp[i][j] = dp[i+1][j]
#      but only if nums[i] < nums[i+1]
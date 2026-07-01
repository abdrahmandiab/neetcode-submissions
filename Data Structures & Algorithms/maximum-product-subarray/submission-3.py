class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        maxi = 0
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
            maxi = max(maxi, nums[i])

        for i in range(n):
            for j in range(i+1,n):
                dp[i][j] = nums[j] * dp[i][j-1]
                maxi = max(maxi,dp[i][j])
        return maxi

# What is the smallest subproblem I am solving?


# Since we are dealing with product, and -ve * -ve = positive, 
# We could need to consider a negative product up to now and a positive one
#  butttt actually we don't -> since the subarray is contiguous
# so the negative thing just tells us, we shouldn't simply break on negative.
# i.e. for [2,4,-3,5] largest is [2,4] -> 2*4 = 8. if we take the -3, it becomes -24
#    and for [-3,1,-2] largest is [-3,1,-2] -> -3*1*-2 = 6. Two negatives made a positive.
# we need to calculate each subarray in the fashion:
#   for i in range(n):
#       for j in range(i+1,n):
#           check(nums[i:j])
# But, this leads to recomputing the same subcomponents of nums[i:j]
#   i.e. ffor nums[0:5], we use the calculation of nums[0:4]*nums[5] and for or nums[0:6] we use nums[0:5]*nums[6]
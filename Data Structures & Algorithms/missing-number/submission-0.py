class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n, xorr = len(nums), len(nums)
        for i in range(n):
            xorr ^= i^nums[i]
        return xorr
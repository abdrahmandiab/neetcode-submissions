class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_mults = [1]*n
        postfix_mults = [1]*n
        for i in range(1,n):
            prefix_mults[i] =  prefix_mults[i-1] *nums[i-1]
            postfix_mults[n-i-1] = postfix_mults[n-i] * nums[n-i]

        for i in range(n):
            prefix_mults[i] = prefix_mults[i] * postfix_mults[i]
        return prefix_mults
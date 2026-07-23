class Solution:
    # def maxCoins(self, nums: List[int]) -> int:
    #     @lru_cache(maxsize=None)
    #     def recur(nums):
    #         nums = list(nums)
    #         res = 0
    #         for j in range(len(nums)):
    #             if j == 0 and len(nums) == 1:
    #                 add = nums[0]
    #             elif j == 0:
    #                 add = nums[0] * nums[1]
    #             elif j == len(nums) - 1:
    #                 add = nums[-1] * nums[-2]
    #             else:
    #                 add = nums[j] * nums[j-1] * nums[j+1]
    #             tmp = nums.pop(j)
    #             res = max(res, recur(tuple(nums)) + add)
    #             nums.insert(j, tmp)
            
    #         return res
        
    #     return recur(tuple(nums))
    def maxCoins(self, nums: List[int]) -> int:
        memo = {}
        def dfs(nums2ple: tuple) -> int:
            if nums2ple in memo:
                return memo[nums2ple]
            nums = list(nums2ple)
            result = 0
            for j in range(len(nums)):
                if j == 0 and len(nums) == 1:
                    add = nums[j]
                elif j==0:
                    add = nums[0] * nums[1]
                elif j == len(nums)-1:
                    add = nums[j-1] * nums[j]
                else:
                    add = nums[j-1] * nums[j] * nums[j+1]
                tmp = nums.pop(j)
                result = max(result, dfs(tuple(nums)) + add)
                nums.insert(j,tmp)
            memo[nums2ple] = result
            return result

        return dfs(tuple(nums))
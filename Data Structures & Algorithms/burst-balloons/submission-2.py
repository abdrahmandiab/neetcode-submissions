from functools import lru_cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def recur(nums):
            nums = list(nums)
            res = 0
            for j in range(len(nums)):
                if j == 0 and len(nums) == 1:
                    add = nums[0]
                elif j == 0:
                    add = nums[0] * nums[1]
                elif j == len(nums) - 1:
                    add = nums[-1] * nums[-2]
                else:
                    add = nums[j] * nums[j-1] * nums[j+1]
                tmp = nums.pop(j)
                res = max(res, recur(tuple(nums)) + add)
                nums.insert(j, tmp)
            
            return res
        
        return recur(tuple(nums))

# the thing we cache for, is the prize for a certain set of balloons_left
# do we need to keep track of cost_so_far?
# 
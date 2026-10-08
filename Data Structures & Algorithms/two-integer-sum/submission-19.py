class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            x = d.get(target-nums[i],-1)
            if x == -1:
                d[nums[i]] = i
            else:
                return [d[target-nums[i]], i]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            x =d.get(target-nums[i],None) 
            if x != None:
                return [x,i]
            d[nums[i]] = i
        return []
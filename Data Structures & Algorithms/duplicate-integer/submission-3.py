class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            if d.get(num,None) != None:
                return True
            else:
                d[num] = 1
        return False
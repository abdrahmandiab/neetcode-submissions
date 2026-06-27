class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        res, l, r = 0,0,0
        while r<n-1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(i+nums[i],farthest)
            l = r+1
            r = farthest
            res+=1
        return res
        
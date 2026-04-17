class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[0]
        while l<=r:
            if nums[l] < nums[r]: #Current chunk is correctly rotated
                res = min(res, nums[l])
                break
                # ^^ This will always bink the result in correctly rotated chunk
            m = (l+r)//2
            res = min(res,nums[m])
            if nums[r] >= nums[m]: # if we're here, then nums[r] < nums[l]
                # case: l (m r)
                r = m - 1
            else:
                # case (l m) r
                l = m+1
        return res


####
# case: l (m r)
# case: (l m) r 
# case: l m r [correctly rotated] CHECK
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if (nums[l] <= nums[m]):
                if (target < nums[l]) or (target > nums[m]):
                    l = m+1
                else:
                    r = m-1
            else: # m in right sorted chunk 
            #  l     m     r
            # [5,6,0,1,2,3,4]
                if target < nums[m] or target > nums[r]:
                    r = m-1
                else:
                    l = m+1
        return -1


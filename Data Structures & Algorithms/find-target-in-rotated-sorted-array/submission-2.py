class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            if nums[l] <= nums[m]: # case 1
                if target > nums[m] or target < nums[l]:
                    l = m+1
                else:
                    r = m-1
            else: # case 2
                if target < nums[m] or target > nums[r]:
                    r = m-1
                else:
                    l = m+1

        return -1

# cases
# case 1: (l m correctly rotated) r
# case 2: l (m r correctly rotated)
# case 3: (l m r correctly rotated)
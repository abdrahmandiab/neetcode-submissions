class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums = [-1,0,1,2,-1,-4]
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            a = nums[i]
            if a>0:
                break
            if i>0 and a==nums[i-1]:
                continue
            lp, rp = i+1, n-1
            while lp<rp:
                tsum = a+ nums[lp] + nums[rp]
                if tsum == 0:
                    res.append([a, nums[lp], nums[rp]])
                    lp+=1
                    rp-=1
                    while nums[lp] == nums[lp-1] and lp < rp:
                        lp+=1
                elif tsum < 0:
                    lp+=1
                else: #tsum > 0
                    rp-=1
                    
        return res


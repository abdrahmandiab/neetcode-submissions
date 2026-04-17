class Solution:
    def trap(self, height: List[int]) -> int:
        nh = len(height)
        lp, rp = 0, nh-1
        lmax, rmax = 0, 0
        tot_wotah = 0
        while lp<rp:
            if height[lp]<height[rp]:
                if height[lp]>= lmax:
                    lmax = height[lp]
                else:
                    tot_wotah+= lmax - height[lp]
                lp+=1
            else: # height[lp] >= height[rp]
                if height[rp]>= rmax:
                    rmax = height[rp]
                else:
                    tot_wotah+= rmax-height[rp]
                rp-=1
        return tot_wotah
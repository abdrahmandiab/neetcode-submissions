class Solution:
    def maxArea(self, heights: List[int]) -> int:
        nh = len(heights)
        lp = 0
        rp = nh-1

        maxWotah = 0

        while lp<rp:
            area = min(heights[lp],heights[rp]) * (rp-lp)
            maxWotah = max(area,maxWotah)
            if heights[lp] <= heights[rp]:
                lp+=1
            else:
                rp-=1

        return maxWotah
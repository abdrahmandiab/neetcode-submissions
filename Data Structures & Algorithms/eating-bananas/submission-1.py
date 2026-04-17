class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we know the ideal scenario is to eat max(piles)/hr
        # so the actual rate is somewhere there
        # so we can binary search the range, calculating the time taken in total to eat all piles
        
        def calculate_total_time(piles: List[int], k: int ):
            tot = 0
            for p in piles:
                tot+= math.ceil(p/k)
            return tot
        
        l, r = 1, max(piles)
        res = r
        while l<= r:
            k = (l+r)//2
            if calculate_total_time(piles, k) <= h:
                # we can keep lowering k further (we want minimum k)
                res = k
                r = k-1 
            else:# total_time > h --> need to increase k
                l = k+1
        return res

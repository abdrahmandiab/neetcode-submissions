class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        pstart, pend =intervals[0] 
        for starti, endi in intervals[1:]:
            if pend < starti: # p[0,1] i[2,3]
                res.append([pstart,pend])
                pstart,pend = starti, endi
                continue
            else: # there is some overlap
                pstart = min(pstart,starti)
                pend = max(pend, endi)
        res.append([pstart,pend])
        return res

# case prev encapsulated in new
# case new encapsulated in prev
# case pstart starti pend endi -> pstart,endi
# case starti pstart endi pend -> starti, pend
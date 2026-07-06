class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removes = 0
        intervals.sort()
        pend = intervals[0][1]
        for start, end in intervals[1:]:
            if pend <= start:
                pend = end
            else:
                removes+=1
                pend = min(pend, end)

        return removes


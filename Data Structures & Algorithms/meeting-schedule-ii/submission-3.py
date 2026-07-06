"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <= 1:
            return len(intervals)
        res = 0
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        sidx = 0
        eidx = 0
        # starts: [0,5,15]
        # ends: [10,20,40]
        rooms = 0
        while sidx <len(intervals):
            if starts[sidx] < ends[eidx]:
                rooms+=1
                sidx+=1
                res = max(res, rooms)
            elif starts[sidx] > ends[eidx]:
                eidx+=1
                rooms-=1
            else:
                sidx+=1
                eidx+=1

        return res

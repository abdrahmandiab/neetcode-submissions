class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        new_start, new_end = newInterval
        for i in range(len(intervals)):
            start_i, end_i = intervals[i]
            if new_end < start_i:
                res.append(newInterval)
                return res+ intervals[i:]
            elif new_start > end_i:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(new_start, start_i),
                    max(new_end, end_i)
                ]
                new_start, new_end = newInterval
        res.append(newInterval)
        return res


# cases:
# 1) there is a slot where it just fits in the middle start_i end_i new_start new_end start_i+1 end_i+1
# 2) it connects two intervals start_i new_start end_i start_i+1 new_end end_i+1
#                           We could do this by extending up: (start_i new_start end_i new_end) -> (start_i -> new_end)
#                           we queue this node again, then extend back (start_i start_i+1 new_end end_i+1) -> (start_i -> end_i+1)
# 3) it extends one interval back
# 4) it extends one interval up

#
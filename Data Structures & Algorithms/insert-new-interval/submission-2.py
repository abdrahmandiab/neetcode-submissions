class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        start_new, end_new = newInterval
        for i in range(len(intervals)):
            start_i, end_i = intervals[i]
            if end_i < start_new:
                res.append(intervals[i])
                continue
            if start_i > end_new:
                res.append(newInterval)
                return res + intervals[i:]
            
            newInterval = [
                min(start_new, start_i),
                max(end_new, end_i)
            ]
            start_new, end_new = newInterval
        res.append(newInterval)

        return res


# cases:
# 1) end of range is 
## 2) it connects two intervals start_i new_start end_i start_i+1 new_end end_i+1
##                           We could do this by extending back: (start_i new_start end_i new_end) -> (start_i -> new_end)
##                           we queue this node again, then extend back (start_i start_i+1 new_end end_i+1) -> (start_i -> end_i+1)
# 3) it extends one interval back
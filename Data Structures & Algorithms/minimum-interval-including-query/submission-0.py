class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]: 
        # queries.sort()
        # intervals.sort()
        res = [-1] * len(queries)
        for i in range(len(queries)):
            curr_min = 99999
            interval_found = False
            for start, end in intervals:
                if start <= queries[i] <= end:
                    curr_min = min(curr_min, end-start+1)
                    interval_found = True
            if interval_found:
                res[i] = curr_min
        return res
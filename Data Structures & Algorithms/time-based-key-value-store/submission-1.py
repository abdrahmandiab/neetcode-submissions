class TimeMap:
    def __init__(self):
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res, values = "" , self.m.get(key,[])
        l,r = 0, len(values)-1
        while l<=r:
            m = (l+r)//2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m+1
            else:
                r = m-1
        return res


# returns,
# most recent value of key
# if set was previously called on it (handled by whether the dict is empty)
# and
# the most recent timestamp for that key (prev_timestamp)
# is <= to the given timestamp (prev_timestamp <= timestamp)
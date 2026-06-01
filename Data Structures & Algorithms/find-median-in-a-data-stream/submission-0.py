class MedianFinder:

    def __init__(self):
        self.small = [] # stores numbers like [0, -2, -5, -8] # ascending order but downwards
        self.large = [] # stores numnbers like [9, 10, 20, 500]

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small,-1 * num)
        
        # balance the heaps
        # Case [0, -2, -5, -8] -> [9, 10]

        # check for other side {+ 1} because we don't balance if diff is only one
        if len(self.small) > len(self.large)+1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small)+1:
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, val)


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-1 * self.small[0] + self.large[0]) /2
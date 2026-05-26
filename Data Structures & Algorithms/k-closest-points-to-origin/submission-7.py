class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        kClos, heap = [], []
        heapq.heapify(heap)

        for p in points:
            heapq.heappush(heap, (self.euclid(p),p))
        print( heap)
        for i in range(k):
            dist, p = heapq.heappop(heap)
            kClos.append(p)
        return kClos
    def euclid(self,p) -> float:
        print(p[0], math.pow(p[1],2))

        return math.sqrt(math.pow(p[0],2) + math.pow(p[1],2))
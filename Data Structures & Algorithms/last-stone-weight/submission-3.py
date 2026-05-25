class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            s1 = heapq.heappop(heap)
            s2 = heapq.heappop(heap)
            if s2 > s1:
                heapq.heappush(heap, s1-s2)     
        return 0 if len(heap)==0 else -heap[0]
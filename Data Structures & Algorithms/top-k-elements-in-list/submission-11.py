class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heapq.heapify(nums)
        freq = defaultdict(int)
        for n in nums:
            freq[n]+=1
        
        heap = []
        for num in freq.keys():
            heapq.heappush(heap,(freq[num],num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        

        return nums[::-k]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out, heap = [] , []
        for i in range(k-1):
            heapq.heappush(heap, (-nums[i], i))
        for i in range(k-1, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            while heap[0][1]<=i-k:
                heapq.heappop(heap)
            out.append(-heap[0][0])
        return out
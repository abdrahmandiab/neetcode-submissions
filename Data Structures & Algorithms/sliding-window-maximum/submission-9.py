class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out, heap = [] , []
        # populate the heap until first window
        for i in range(k-1):
            heapq.heappush(heap, (-nums[i], i))
        # For each window after:
        #    pop from the heap until the top (max) element's index is within range
        #    append the top element to output (without popping it)
        for r in range(k-1, len(nums)):
            heapq.heappush(heap, (-nums[r], r))
            while heap[0][1]<=r-k:
                heapq.heappop(heap)
            out.append(-heap[0][0])
        return out
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        occur = Counter(tasks).values()
        negHeap = [-cnt for cnt in occur]
        heapq.heapify(negHeap)
        time = 0
        q = deque()
        while negHeap or q:
            time+=1
            if not negHeap:
                time = q[0][1]
            else:
                cnt = 1+ heapq.heappop(negHeap)
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(negHeap, q.popleft()[0])
        return time
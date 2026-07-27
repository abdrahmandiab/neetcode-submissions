class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v,t))
        visit = set()
        minHeap =[(0,k)]
        t = 0
        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = t1

            for n2, t2 in graph[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (t1+t2, n2))

        return t if len(visit) == n else -1

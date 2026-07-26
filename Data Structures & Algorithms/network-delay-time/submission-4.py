class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v,w))
        
        dist = {i: float('inf') for i in range(1 ,n+1)}
        dist[k] = 0

        pq = [(0,k)]

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue
            
            for v, weight in graph[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v],v))

        max_dist = max(dist.values())
        return max_dist if max_dist != float('inf') else -1
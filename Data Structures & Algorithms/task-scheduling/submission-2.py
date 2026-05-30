class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hp, q = [], deque([])
        for k, v in Counter(tasks).items():
            heapq.heappush(hp, (-v,k))
        t=0
        while q or hp:
            if hp:
                freq, task = heapq.heappop(hp)
                t+=1
                freq+=1
                if freq<0: #still some time left
                    q.append((t+n, freq, task))
            if not q:
                continue
            
            if t>=q[0][0]:
                _, freq, p = q.popleft()
                heapq.heappush(hp, (freq,p))
            else:
                if not hp:
                    t = q[0][0]
        return t
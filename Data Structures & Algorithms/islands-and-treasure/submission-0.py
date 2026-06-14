class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        tcs = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def update_costs(r,c):
            visit = set()
            q = deque()
            q.append((r,c, 0))
            visit.add((r,c))
            while q:
                row, col, cost = q.popleft()
                for dr, dc in directions:
                    r,c = row+dr, col+dc
                    if (r in range(m) and c in range(n) and
                        grid[r][c]!= -1 and (r,c) not in visit):
                        visit.add((r,c))
                        grid[r][c] = min(grid[r][c], cost+1)
                        q.append((r,c,cost+1))

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    tcs.add((r,c))
        
        for tr, tc in tcs:
            update_costs(tr,tc)
        
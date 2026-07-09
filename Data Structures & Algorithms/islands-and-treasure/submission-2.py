class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(r,c):
            q.append((r,c,1))
            while q:
                r, c, cost_so_far = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (nr in range(ROWS) and nc in range(COLS)
                    and grid[nr][nc] > 0 and cost_so_far < grid[nr][nc]):
                        grid[nr][nc] = cost_so_far
                        q.append((nr,nc,cost_so_far+1))        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    bfs(r,c)



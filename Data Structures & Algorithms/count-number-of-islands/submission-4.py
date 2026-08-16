class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        def bfs(r,c):
            q = deque([(r,c)])
            visit.add((r,c))
            print(q)
            while q:
                x = q.popleft()
                print(x)
                row, col = x
                for dr,dc in dirs:
                    nr, nc = row+dr, col+dc
                    if (nr in range(ROWS) and nc in range(COLS)
                    and ((nr,nc) not in visit) and grid[nr][nc] == "1"):
                        q.append((nr,nc))
                        visit.add((nr,nc))

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    islands+=1
                    bfs(r,c)
        return islands

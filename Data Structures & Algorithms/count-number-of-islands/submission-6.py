class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        ROWS, COLS = len(grid), len(grid[0])
        rROWS, rCOLS = range(ROWS), range(COLS)
        visit = set()
        def bfs(r,c):
            q = deque([(r,c)])
            visit.add((r,c))
            while q:
                x = q.popleft()
                row, col = x
                for dr,dc in dirs:
                    nr, nc = row+dr, col+dc
                    if (nr in rROWS and nc in rCOLS
                    and ((nr,nc) not in visit) and grid[nr][nc] == "1"):
                        q.append((nr,nc))
                        visit.add((nr,nc))

        islands = 0
        for r in rROWS:
            for c in rCOLS:
                if grid[r][c] == "1" and (r,c) not in visit:
                    islands+=1
                    bfs(r,c)
        return islands

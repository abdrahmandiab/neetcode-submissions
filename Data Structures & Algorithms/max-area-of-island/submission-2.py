class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1] * (n+1)

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node] # the root
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        if self.size[pu] >= self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv
        return True


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def index(r,c):
            return (r*COLS) + c

        dsu = DSU(ROWS*COLS)
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        area_found = False
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area_found = True
                    for dr, dc in dirs:
                        nr, nc = r+dr, c + dc
                        if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1:
                            dsu.union(index(r,c), index(nr,nc))
        return max(dsu.size) if area_found else 0
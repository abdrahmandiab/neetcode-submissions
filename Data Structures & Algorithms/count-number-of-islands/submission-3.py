class DSU:
    def __init__(self,n) -> None:
        self.Parent = list(range(n+1)) # [1,2,3,4,...,n-1,n]
        self.Size = [1] * (n+1) # [1,1,1,1,...,1,1]

    def find(self, node) -> int:
        if self.Parent[node] != node: # if parent[1] != 1
            self.Parent[node] = self.find(self.Parent[node]) # recursively find the parent until root.
        return self.Parent[node] # root
    
    def union(self, u, v) -> bool:
        pu = self.find(u) # parent of first node
        pv = self.find(v) # parent of second node

        if pu == pv: # if they already share the same node
            return False
        if self.Size[pu] >= self.Size[pv]:
            self.Size[pu] += self.Size[pv]
            self.Parent[pv] = pu
        else:
            self.Size[pv] += self.Size[pu]
            self.Parent[pu] = pv
        return True


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        dsu = DSU(ROWS*COLS)
        def index(r,c):
            return (r * COLS) +c
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" :
                    islands+=1
                    for dr, dc in directions:
                        row, col = r+dr, c+dc
                        if (row in range(ROWS) and col in range(COLS) 
                        and grid[row][col] == "1" and dsu.union(index(r,c), index(row,col))):
                            islands-=1
        return islands


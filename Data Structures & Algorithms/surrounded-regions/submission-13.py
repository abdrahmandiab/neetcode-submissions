class DSU:
    def __init__(self, n):
        self.size = [1] * (n+1)
        self.parent = list(range(n+1))
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

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

    def connected(self, u, v):
        return self.find(u) == self.find(v) # same roots

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        dsu = DSU(ROWS*COLS+1)
        def index(r,c):
            return (r*COLS) + c

        dirs = [[1,0], [-1,0],[0,1],[0,-1]]
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] != "O":
                    continue
                if (r ==0 or c ==0 
                    or r== (ROWS-1) or (c == COLS-1)):
                    dsu.union(ROWS*COLS, index(r,c))
                else:
                    for dr, dc in dirs:
                        nr,nc = r+dr, c+dc
                        if board[nr][nc] == "O":
                            dsu.union(index(r,c), index(nr,nc))
        for r in range(ROWS):
            for c in range(COLS):
                if not dsu.connected(ROWS*COLS, index(r,c)):
                    board[r][c] = "X"
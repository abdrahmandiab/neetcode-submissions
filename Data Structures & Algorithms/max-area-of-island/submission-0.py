class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxArea = 0
        visit = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))
            area=1
            while q:
                r,c = q.popleft()
                for dr, dc in directions:
                    row, col = r+dr, c + dc
                    if (row in range(ROWS) and
                        col in range(COLS) and
                        grid[row][col] == 1 and
                        (row,col) not in visit):
                            q.append((row,col))
                            visit.add((row,col))
                            area+=1
            self.maxArea = max(self.maxArea, area)

        for r in range(ROWS):
            for c in range(COLS):
                if (grid[r][c]==1 and (r,c) not in visit):
                    bfs(r,c) 

        return self.maxArea
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        fresh = 0
        rotten = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] ==2:
                    rotten+=1

        directions = [[1,0],[-1,0],[0,1], [0,-1]]
        if rotten ==0:
            if fresh == 0:
                return 0
            return -1
        minutes = 0
        q = deque()
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c,0))

        while q:
            r,c,time_elapsed = q.popleft()
            for dr,dc in directions:
                nr, nc = r+dr, c+dc
                if (nr in range(ROWS) and nc in range(COLS)
                    and grid[nr][nc] == 1): 
                        fresh-=1
                        minutes = max(minutes, time_elapsed+1)
                        grid[nr][nc] = 2
                        q.append((nr,nc,time_elapsed+1))

        return minutes if fresh == 0 else -1
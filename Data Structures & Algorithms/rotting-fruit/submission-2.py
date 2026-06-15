class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        time=0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def rotify(r,c):
            nonlocal fresh, ROWS, COLS
            if (r in range(ROWS) and c in range(COLS) and grid[r][c] == 1):
                grid[r][c] = 2
                fresh-=1
                return True
            return False
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh+=1
        if len(q) == 0: # rotten = 0
            return 0 if fresh == 0 else -1
        # rotten > 0, fresh > 0
        while q and fresh>0:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    app_true = rotify(r,c)
                    if app_true:
                        q.append((r,c))
            time+=1


        return time if fresh == 0 else -1

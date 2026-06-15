class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        pacific = [tuple(p) for p in ([0,i] for i in range(COLS))] + [(i,0) for i in range(ROWS)]
        pac_touch = [[False]* COLS for _ in range(ROWS)]
        atlantic = [tuple(p) for p in ([ROWS-1,i] for i in range(COLS)) ] + [(i,COLS-1) for i in range(ROWS)]
        atl_touch = [[False]* COLS for _ in range(ROWS)]
        
        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (nr in range(ROWS) and nc in range(COLS)
                    and not ocean[nr][nc] and heights[nr][nc] >= heights[r][c]):
                        q.append((nr,nc))
        bfs(pacific, pac_touch)
        bfs(atlantic, atl_touch)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac_touch[r][c] and atl_touch[r][c]:
                    res.append([r,c])

        return res
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        touch_pac = []
        touch_atl = []
        for r in range(ROWS):
            touch_pac.append((r,0))
            touch_atl.append((r,COLS-1))

        for c in range(COLS):
            touch_pac.append((0,c))
            touch_atl.append((ROWS-1,c))

        def bfs(starts):
            nonlocal dirs, heights
            visited = set(starts)
            q = deque(starts)
            while q:
                r,c = q.popleft() # extract from queue or loop
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if (nr in range(ROWS) and nc in range(COLS)
                        and (nr,nc) not in visited and heights[nr][nc]>= heights[r][c]):
                            visited.add((nr,nc))
                            q.append((nr,nc))
                            
            return visited

        pac = bfs(touch_pac)
        atl = bfs(touch_atl)
        ret = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    ret.append([r,c])
        return ret

# UDLR
# equal or lower water

# return: [[r,c]] where r,c touches both pacific and atlantic


# left column (c = 0) all pacific
# right column (c=COLS-1) all atlantic
# top row (r=0) all pacific
# bottom row (row=ROWS-1) all atlantic
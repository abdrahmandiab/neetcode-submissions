class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        starts = []
        for r in range(ROWS):
            if board[r][0] == "O":
                board[r][0] = "T"
                starts.append((r,0))
            if board[r][COLS-1] == "O":
                board[r][COLS-1] = "T"
                starts.append((r,COLS-1))
        for c in range(COLS):
            if board[0][c] == "O":
                board[0][c] = "T"
                starts.append((0,c))
            if board[ROWS-1][c] == "O":
                board[ROWS-1][c] = "T"
                starts.append((ROWS-1,c))
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(starts):
            q = deque(starts)
            while q:
                r,c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if (nr in range(ROWS) and nc in range(COLS)
                    and board[nr][nc] =="O"):
                        board[nr][nc] = "T"
                        q.append((nr,nc))

        bfs(starts)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] =="T":
                    board[r][c] = "O"

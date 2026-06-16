class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS = len(board), len(board[0])
        rROWS, rCOLS = range(ROWS), range(COLS)
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        q = deque()
        for r in rROWS:
            if board[r][0] == "O":
                board[r][0] = "T"
                q.append((r,0))
            if board[r][COLS-1] == "O":
                board[r][COLS-1] = "T"
                q.append((r,COLS-1))
        for c in rCOLS:
            if board[0][c] == "O":
                board[0][c] = "T"
                q.append((0,c))
            if board[ROWS-1][c] == "O":
                board[ROWS-1][c] = "T"
                q.append((ROWS-1, c))
        while q:
            row,col = q.popleft()
            for dr,dc in directions:
                r, c = dr+row, dc+col
                if (r in rROWS and c in rCOLS
                    and board[r][c]=="O"):
                    board[r][c] = "T"
                    q.append((r,c))

        for r in rROWS:
            for c in rCOLS:
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"
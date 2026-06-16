class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS, o = len(board), len(board[0]), "O"
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        q = deque()
        for r in range(ROWS):
            if board[r][0] == o:
                q.append((r,0))
            if board[r][COLS-1] == o:
                q.append((r,COLS-1))
        for c in range(COLS):
            if board[0][c] == o:
                q.append((0,c))
            if board[ROWS-1][c] == o:
                q.append((ROWS-1, c))
        # now q = [3,1] (the only border o pos)
        print(list(q))
        while q:
            row,col = q.popleft()
            board[row][col] = "T"
            for dr,dc in directions:
                r, c = dr+row, dc+col
                if (r in range(ROWS) and c in range(COLS)
                    and board[r][c]=="O"):
                    q.append((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"
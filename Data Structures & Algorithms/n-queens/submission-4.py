class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ret = []
        board = [["."] * n for i in range(n)] # n*n board
        def backtrack(row):
            #queen's colition is row = row, column = element from remaining_cols
            if row == n:
                copied = ["".join(row) for row in board]
                ret.append(copied)
                return
            for col in range(n):
                use_pos = True
                if self.no_intersects(row,col,board):
                    board[row][col] = "Q"
                    backtrack(row+1)  
                    board[row][col] = "."
        backtrack(0)
        return ret

    def no_intersects(self,row, col, board):
        # all other queens are above me
        for r_above in range(row,-1,-1):
            if board[r_above][col] == "Q":
                return False
        r, c = row-1, col-1
        while r>=0 and c>=0:
            if board[r][c] == "Q":
                return False
            r-=1
            c-=1
        
        r, c = row-1, col+1
        while r>=0 and c < len(board):
            if board[r][c] =="Q":
                return False
            r-=1
            c+=1
        return True


# We need to reduce problem space so we can make a tree.
# since we know n == num queens == board dims
# there will be one queen per row.
# So we can choose the branching based on the COLUMN we place Q in.
# so tree  for n=3 looks like
#                       root
#           Q1-C1                  Q1-C2                    Q1-C3   
#   Q2-C1x Q2-C2x Q2-C3y    Q2-C1x Q2-C2x Q2-C3x       Q2-C1 Q2-C2x
#              Q3-C2x                               Q3-C2x



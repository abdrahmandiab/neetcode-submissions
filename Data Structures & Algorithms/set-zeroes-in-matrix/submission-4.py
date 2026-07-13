class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_cols = set()
        zero_rows = set()
        ROWS,COLS = len(matrix), len(matrix[0])
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] ==0:
                    zero_cols.add(c)
                    zero_rows.add(r)
        for r in range(ROWS):
            if r not in zero_rows:
                continue
            for c in range(COLS):
                matrix[r][c] = 0
        for c in range(COLS):
            if c not in zero_cols:
                continue
            for r in range(ROWS):
                matrix[r][c] = 0
        
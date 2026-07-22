class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        ROWS, COLS = len(matrix), len(matrix[0])
        rrows, rcols = range(ROWS), range(COLS)
        
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        
        def dfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            max_len = 1
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if nr in rrows and nc in rcols and matrix[nr][nc] > matrix[r][c]:
                    max_len = max(max_len, 1+ dfs(nr,nc))
            memo[(r,c)] = max_len
            return max_len
        
        maxi = 0
        for r in rrows:
            for c in rcols:
                maxi = max(dfs(r,c), maxi)
        return maxi
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS,COLS = m,n
        dp = [[0]*COLS for _ in range(ROWS)]
        dp[0] = [1]*COLS
        for r in range(ROWS):
            dp[r][0] = 1
        

        for i in range(1,ROWS,1):
            for j in range(1,COLS,1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

#  base condition
#       rows are m
#       cols are n
#       go right, or go down (if both in range)
#  otherwise: we are forced to go right when i == bottom
#             we are forced to go down when j == bottom
#  dp[i][j] = how many paths path through here?
#  dp[i][j] = sum of (top cell path value + left cell path value)
#  dp[i][j] = dp[i-1][j] + dp[i][j-1]
#  dp[top row] = 1 -> 
#  dp[left side] = 1
#  result = dp[m][n]

# e.g. we can go down down
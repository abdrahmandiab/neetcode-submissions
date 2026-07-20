class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n, m = amount+1, len(coins)
        # m to iterate along rows
        # n to iterate along cols
        #         amount +1      
        #          5  4  3  2  1  0
        # coins  1             1  1
        #        2                1
        #.       %                1
        dp = [[0]*n for _ in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if j == amount:
                    dp[i][j] = 1
                    continue
                f,s = 0,0
                if i+1 < m:
                    f = dp[i+1][j]
                if (j+coins[i]) < n :
                    s = dp[i][j+coins[i]]
                dp[i][j] = f + s
        return dp[0][0]


# recurrence relation is
# dp[i][j] = dp[i+1][j](cell below) + dp[i][j+coins[i]] (cell coins value to right if in range)
# start from bottom-most, 1 before right most, a.k.a.
# bottom most = m , right most -1 = n-1
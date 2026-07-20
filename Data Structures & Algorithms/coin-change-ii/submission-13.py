class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        lc = len(coins)
        def dfs(i, total):
            if total == amount:
                return 1
            if i == lc or total > amount:
                return 0 
            if (i,total) in dp:
                return dp[(i,total)]
            dp[(i,total)] = dfs(i+1, total) + dfs(i, total + coins[i])
            return dp[(i,total)]
        return dfs(0,0)
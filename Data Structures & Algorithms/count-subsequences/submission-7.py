class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(m+1):
            dp[i][-1] = 1 # set end of every row to 1 (a.k.a. last column)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]
        # def dfs(i,j):
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     num_distinct = 0
        #     if j >= len(t):
        #         return 1
        #     if i >= len(s):
        #         return 0
        #     if s[i] == t[j]: # c == c, or t == t
        #         num_distinct = dfs(i+1,j+1) # take char
        #     num_distinct += dfs(i+1,j) # don't take char - forced if chars don't match
        #     memo[(i,j)] = num_distinct
        #     return num_distinct
        return dp[0][0]

 
# for each sub variation i,j
# we are repeatedly asking what is the num distinct subsequences we can get from i,j together
# so dp[i][j] = how many distinct subsequnces we can get for s[i:], t[j:]
#    we can assume the base case that s[i=m:] t[j=n:] is 0 -> if both strings empty, return 0
#                              further, if s = "" or j = "", we can also return 0
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            num_distinct = 0
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0
            if s[i] == t[j]: # c == c, or t == t
                num_distinct = dfs(i+1,j+1) # take char
            num_distinct += dfs(i+1,j) # don't take char - forced if chars don't match
            memo[(i,j)] = num_distinct
            return num_distinct
        return dfs(0,0)

# at every point
# take or leave the letter IFF it matches the letter from t
# i.e. if s[i] == s[j]: dfs(i+1,j+1)
#     dfs(i+1,j) anyway
#  
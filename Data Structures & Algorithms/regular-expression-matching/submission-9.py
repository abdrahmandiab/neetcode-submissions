class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls, lp = len(s), len(p)
        memo = {}
        def dfs(i,j):
            if j == lp:
                return i == ls
            if (i,j) in memo:
                return memo[(i,j)]
            first_match = i<ls and (s[i] == p[j] or p[j] == ".")
            # i<ls enforces:
            #     i still not at the end.
            memo[(i,j)] = False
            if (j+1) < lp and p[j+1] == "*":
                memo[(i,j)] = (dfs(i, j+2) or (first_match and dfs(i+1,j)))
                return memo[(i,j)]
            if first_match:
                memo[(i,j)] = dfs(i+1,j+1)
            return memo[(i,j)]
        return dfs(0,0)
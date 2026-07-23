class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls, lp = len(s), len(p)
        dp = [[False]*(lp+1) for _ in range(ls+1)]
        dp[ls][lp] = True

        for j in range(lp-1,-1,-1):
            if j+1 < lp and p[j+1] == "*":
                dp[ls][j] = dp[ls][j+2]

        for i in range(ls,-1,-1):
            for j in range(lp-1,-1,-1):
                first_match = i< ls and (s[i] == p[j] or p[j] == ".")
                if first_match:
                    dp[i][j] = dp[i+1][j+1]
                if j+1 < lp and p[j+1] == "*":
                    # dp[i][j+2]: 0 occurences of p[j]*
                    # dp[i+1][j]: 1+ occurences (if first_match is True)
                    dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])
        return dp[0][0]
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <2:
            return s
        dp = [[False]* n for _ in range(n)]

        start_idx, lenny = 0, 1
        # The diagonal
        for i in range(n):
            dp[i][i] = True
        
        # adjacent pairs
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start_idx, lenny = i,2

        # Recurrence
        lengths = range(3,n+1)
        for length in lengths:
            for i in range(n-length+1):
                j = i+length-1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    start_idx, lenny = i, length

        return s[start_idx: start_idx + lenny]



# For a moment, let me 
#
#
#
#
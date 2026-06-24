class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        
        # Handle both cases (len(1), len(2))
        dp[n-1][n-1] = True
        count = 1
        for i in range(n-1):
            dp[i][i] = True
            count+=1
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                count+=1
        
        lengths = range(3,n+1)
        for length in lengths:
            # for length 3
            # we want i to go over 0, [i.e. range(0 -> n-length+1)]
            for i in range(n-length+1):
                j = i+length-1 # max j should be 2
                if (s[i]==s[j] and dp[i+1][j-1]):
                    dp[i][j] = True
                    count+=1
        return count
        
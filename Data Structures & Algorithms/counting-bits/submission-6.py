class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        latest_pow = 1
        for i in range(1, n+1):
            if i == 2* latest_pow:
                latest_pow = i
                print(i, latest_pow)
            dp[i] = 1 + dp[i - latest_pow]
        return dp
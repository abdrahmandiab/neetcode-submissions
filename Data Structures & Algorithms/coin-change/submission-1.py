class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1) 
        dp[0] = 0
        for a in range(1, amount+1):
            for c in coins:
                if a-c >=0:
                    dp[a] = min(dp[a],1 + dp[a-c])
        return dp[amount] if dp[amount] != amount+1 else -1




# Game plan:
# We want to basically have a tree structure where 
# At each turn, we make the decision:
#     Use a coin from this denomination, or not.
# Until the goal is reached.

# We 
#  

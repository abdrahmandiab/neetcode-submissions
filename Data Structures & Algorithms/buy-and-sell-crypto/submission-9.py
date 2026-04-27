class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp, rp = 0, 1
        profit = 0
        while rp<len(prices):
            if prices[lp] < prices[rp]:
                new_profit = prices[rp] - prices[lp]
                profit = max(profit, new_profit)
            else:
                lp = rp
            rp+=1
        return profit

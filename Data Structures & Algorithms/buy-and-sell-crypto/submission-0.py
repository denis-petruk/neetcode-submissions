class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        entry, profit = prices[0],0
        for i in prices:
            profit = max(profit,i - entry)           
            if i <= entry:
                entry = i
        return profit 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        bought = prices[0]
        for i in prices:
            margin = i - bought
            if  margin > 0:
                profit += margin
            bought = i
        return profit
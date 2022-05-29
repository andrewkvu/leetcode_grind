class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        currentBuy = 10000
        for val in prices:
            if val < currentBuy:
                currentBuy = val
            elif val - currentBuy > profit:
                profit = val - currentBuy
        return profit
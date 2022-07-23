class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window
        res = 0
        left = 0
        
        for right in range(1, len(prices)):
            # look for lowest price and set left index to right
            if prices[right] < prices[left]: 
                left = right
            # find max profit based on left and right prices
            res = max(res, prices[right] - prices[left])
        
        return res
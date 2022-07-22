class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        dp = [float('inf')] * (amount + 1) # max float placeholder to eventually compute min coins
        dp[0] = 0 # takes 0 coins to amount to 0

        for amt in range(1, amount + 1): # computing the dp array for each amount leading upto amount
            for c in coins:
                if amt - c >= 0: # nonnegative result for current amount - one of the coins
                    dp[amt] = min(dp[amt], 1 + dp[amt - c])
                    # coin c = 4
                    # amt = 7
                    # dp[7] = min(dp[7], 1 + dp[7 - 4 = 3])
                    # where 1 is 1 c coin
        # print(dp)
        return dp[amount] if dp[amount] != float('inf') else -1
        
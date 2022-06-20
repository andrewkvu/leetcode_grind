class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0] = cost[0] # base case
        dp[1] = cost[1] # base case

        for i in range(2, len(cost)):
            # recurrence relation
            dp[i] = cost[i] + min(dp[i - 2], dp[i - 1])

        # since the minimum cost can be in the last two indexes, return minimum between those
        return min(dp[-1], dp[-2])
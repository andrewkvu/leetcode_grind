class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        pass1, pass7, pass30 = 0, 1, 2
        travelDays = set(days)
        lastDay = days[-1] # 20
        
        dp = [0 for i in range(lastDay + 1)] # include 20 in dp array
        
        for day in range(1, lastDay + 1):
            if day not in travelDays: # if you don't travel on this day
                dp[day] = dp[day - 1] # just set the value to the previous day's
            else:
                dp[day] =   min(dp[day - 1] + costs[pass1], 
                            dp[max(day - 7, 0)] + costs[pass7], # max condition if eg 4-7 no index
                            dp[max(day - 30, 0)] + costs[pass30])
        return dp[lastDay]
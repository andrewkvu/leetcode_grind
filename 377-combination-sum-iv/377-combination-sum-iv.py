class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0 : 1} # base case 1 way to sum up to 0

        for total in range(1, target + 1):
            dp[total] = 0
            for num in nums: # can get diff # combinations per coin value
                dp[total] += dp.get(total - num, 0) # in case of negative case

        return dp[target]
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1 for i in range(N)]

        for i in range(N - 1, -1, -1): # go backwards
            # check all the subsequence potentials from i to N
            # 7-7, 6-7, 5-6-7, 4-5-6-7, where i is the first number, j are the numbers following
            for j in range(i + 1, N): 
                if nums[i] < nums[j]: # this means there's an increasing subsequence
                    dp[i] = max(dp[i], 1 + dp[j]) 
                    # len of subsequence is just increasing the one already calculated from j
                    # only dp[i] changes, the j's that you keep iterating through are
                    # static after their initial change
        return max(dp)
        
        
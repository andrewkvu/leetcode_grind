class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # take the max excluding the 1st house and excluding the last house
        # since the circular effect only affects the first and last houses
        return max(self.rob1(nums[:-1]), self.rob1(nums[1:]))
        
    # exact same from house robber 1
    def rob1(self, nums):
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            
        return dp[-1]
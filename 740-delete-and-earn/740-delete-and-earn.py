class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # kinda like house robber, but you have to stack the points per number
        # 2 2 3 3 3 4 == 4 9 4, but you use a big array like 10001 so that its easier to put 
        # after that just house robber
        if len(nums) == 1:
            return nums[0]
        dp = [0] * 10001
        
        points = [0] * 10001
        
        for num in nums:
            points[num] += num
        
        
        dp[0] = points[0]
        dp[1] = max(points[0], points[1])
        
        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 2] + points[i], dp[i - 1])
        
        return max(dp)
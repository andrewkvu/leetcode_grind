class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = grid
        ROWS = len(dp)
        COLS = len(dp[0])
        
        for i in range(1, ROWS):
            dp[i][0] += dp[i - 1][0]
        for j in range(1, COLS):
            dp[0][j] += dp[0][j - 1]
        
        for i in range(1, ROWS):
            for j in range(1, COLS):
                dp[i][j] += min(dp[i][j - 1], dp[i - 1][j])
        
        return dp[-1][-1]
        
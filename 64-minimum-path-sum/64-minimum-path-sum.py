class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = grid
        ROWS = len(dp)
        COLS = len(dp[0])
        
        # start at 1 because [0][0] is already good
        for i in range(1, ROWS): # do first column
            dp[i][0] += dp[i - 1][0]
        for j in range(1, COLS): # do first row
            dp[0][j] += dp[0][j - 1]
        
        # compute for the rest of the squares since now you have all starting paths
        # from top left to bottom right
        for i in range(1, ROWS):
            for j in range(1, COLS):
                dp[i][j] += min(dp[i][j - 1], dp[i - 1][j])
        
        return dp[-1][-1]
        
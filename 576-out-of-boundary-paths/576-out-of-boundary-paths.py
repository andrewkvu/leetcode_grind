class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # modification of brute force basically        
        # 3D DP declaration
        dp = [([[-1] * (maxMove + 1) for i in range(n + 1)]) for j in range(m + 1)]
        
        def find(maxMove, startRow, startColumn):
            if startRow < 0 or startColumn < 0 or startRow >= m or startColumn >= n:
                return 1 # out of bounds = 1
            if maxMove == 0:
                return 0 # out of moves and its in bounds = can't do any path
            if dp[startRow][startColumn][maxMove] != -1: # if the initial -1 changed
                return dp[startRow][startColumn][maxMove] # don't recalculate
            # brute force graph movement stored into the DP array
            dp[startRow][startColumn][maxMove] = \
               (find(maxMove - 1, startRow + 1, startColumn) \
            +   find(maxMove - 1, startRow - 1, startColumn) \
            +   find(maxMove - 1, startRow, startColumn + 1) \
            +   find(maxMove - 1, startRow, startColumn - 1))
            
            return dp[startRow][startColumn][maxMove]
        
        MOD = 10 ** 9 + 7
        return find(maxMove, startRow, startColumn) % MOD
            
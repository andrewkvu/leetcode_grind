class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [([[-1] * (maxMove + 1) for i in range(n + 1)]) for j in range(m + 1)]
        
        def find(maxMove, startRow, startColumn):
            if startRow < 0 or startColumn < 0 or startRow >= m or startColumn >= n:
                return 1
            if maxMove == 0:
                return 0
            if dp[startRow][startColumn][maxMove] != -1:
                return dp[startRow][startColumn][maxMove]
            dp[startRow][startColumn][maxMove] = \
               (find(maxMove - 1, startRow + 1, startColumn) \
            +   find(maxMove - 1, startRow - 1, startColumn) \
            +   find(maxMove - 1, startRow, startColumn + 1) \
            +   find(maxMove - 1, startRow, startColumn - 1))
            
            return dp[startRow][startColumn][maxMove]
        
        return find(maxMove, startRow, startColumn) % MOD
            
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # same as longestIncreasingPath for the most part
        # just += for res to find the number of paths instead of the longest path
        
        ROWS, COLS = len(grid), len(grid[0])
        MOD = 10 ** 9 + 7
        dp = {} # (r, c) -> numPaths

        def dfs(r, c, prevPathVal):
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] <= prevPathVal:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            res = 1
            res += dfs(r + 1, c, grid[r][c])
            res += dfs(r - 1, c, grid[r][c])
            res += dfs(r, c + 1, grid[r][c])
            res += dfs(r, c - 1, grid[r][c])

            dp[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, 0)

        # print(dp)

        return sum(dp.values()) % MOD
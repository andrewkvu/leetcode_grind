class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # graph traversal with a hashmap for dp
        # 1 + to add onto length of path
        # keep track of the prevPathLen so that you can add 1 to it
        # update dp[(r, c)] to res and return res
        
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {} # (r,c) -> LIP

        def dfs(r, c, prevPathLen):
            if r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prevPathLen: # strictly increasing <=
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))

            dp[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)

        return max(dp.values())
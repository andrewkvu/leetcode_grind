class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        ROWS = len(heights)
        COLS = len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, heightBefore):
            # like a diagonal wave border,
            # if current height is less than the previous height used
            # it's not in the same ocean
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or \
            (r, c) in visited or heights[r][c] < heightBefore:
                return
            visited.add((r, c)) # conditions met for adding to respective ocean border
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # finds all the cells in each ocean based on rows
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0]) # 0th column always borders pacific
            dfs(r, COLS - 1, atl, heights[r][COLS - 1]) # last column always borders atlantic

        # finds all the cells in each ocean based on cols
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c]) # 0th row always borders pacific
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c]) # last row always borders atlantic

        # check which r, c intersects atl and pac for the rainspots
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
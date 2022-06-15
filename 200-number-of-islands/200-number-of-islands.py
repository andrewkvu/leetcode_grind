class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
    
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(grid, r, c):
            # if out of bounds, or the position has already been visited, or position is 0
            # we don't want to check it
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or grid[r][c] == "0":
                return
            visited.add((r, c)) # adds position tuple to visited
            dfs(grid, r + 1, c) # goes right till it can't anymore
            dfs(grid, r - 1, c) # go left
            dfs(grid, r, c + 1) # go up
            dfs(grid, r, c - 1) # go down

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(grid, r, c)
                    islands += 1

        return islands
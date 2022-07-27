class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res = []
        ROWS = len(land)
        COLS = len(land[0])
        visited = set()

        def dfs(r, c, visited):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS \
                    or land[r][c] == 0 or (r, c) in visited:
                return (0, 0)

            visited.add((r, c))
            # only need to check increasing since the plots of land are rectangular
            r1, c1 = dfs(r + 1, c, visited)
            r2, c2 = dfs(r, c + 1, visited)

            maxR = max(r, r1, r2)
            maxC = max(c, c1, c2)

            return (maxR, maxC)

        for r in range(ROWS):
            for c in range(COLS):
                if land[r][c] == 1 and (r, c) not in visited:
                    r1, c1 = dfs(r, c, visited)
                    res.append([r, c, r1, c1])

        return res
        
        
        
        
        
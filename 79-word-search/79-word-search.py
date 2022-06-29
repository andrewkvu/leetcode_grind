class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # find first character, then dfs from there
        # find the out of bounds and yeah
        ROWS = len(board)
        COLS = len(board[0])
        seenTuple = set()
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in seenTuple or board[r][c] != word[i]:
                return False
            # add for this specific path that we are trying to find
            seenTuple.add((r, c))
            
            res =   dfs(r + 1, c, i + 1) or \
                    dfs(r - 1, c, i + 1) or \
                    dfs(r, c + 1, i + 1) or \
                    dfs(r, c - 1, i + 1) 
            
            # so we can use this path for another iteration of DFS since we don't want it always seen
            seenTuple.remove((r, c))
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        return False
            
        
        
        
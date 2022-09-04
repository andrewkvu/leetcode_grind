class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set() # r + c
        negDiag = set() # r - c
        res = []

        board = [["."] * n for i in range(n)] # init n x n board

        def backtrack(r):
            if r == n: # made it to last row of the board
                validBoard = ["".join(row) for row in board] # string format for prompt
                res.append(validBoard)
                return

            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag: # can't place a queen here
                    continue
                # appending/adding part
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = 'Q'

                backtrack(r + 1) # deepest solution

                # popping/removing part
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = '.'

        backtrack(r = 0)
        return res
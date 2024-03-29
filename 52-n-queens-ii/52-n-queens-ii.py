class Solution:
    def totalNQueens(self, n: int) -> int:
        # same as N-Queens but no need for board
        cols = set()
        posDiag = set()
        negDiag = set()
        res = 0

        def backtrack(r):
            if r == n:
                nonlocal res
                res += 1

            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                backtrack(r + 1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(r = 0)
        return res
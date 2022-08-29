class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        diagonals = defaultdict(list)

        # store the diagonal values in a map
        for r in range(ROWS):
            for c in range(COLS):
                diagonals[r - c].append(mat[r][c])
        # print(diagonals)

        # sort the diagonals in reverse order to save space
        for d in diagonals:
            diagonals[d].sort(reverse = True)
        # print(diagonals)

        # set the values equal to the popped version of the dictionary since its in reverse, saving space
        for r in range(ROWS):
            for c in range(COLS):
                mat[r][c] = diagonals[r - c].pop()
        # print(diagonals)

        return mat
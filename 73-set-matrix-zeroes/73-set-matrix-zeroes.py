class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])

        # mark if the first row or column has a 0, and convert those last
        firstCol = False
        firstRow = False

        for r in range(ROWS):
            if matrix[r][0] == 0:
                firstCol = True
                break
        for c in range(COLS):
            if matrix[0][c] == 0:
                firstRow = True
                break

        # go from 1,1 to the end, find all zeroes and 
        # mark their columns and rows in the first position 
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # set all cells that have a 0 in their first row or column position to 0
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # set all the first column and row cells to 0 if its true
        if firstCol:
            for r in range(ROWS):
                matrix[r][0] = 0
        if firstRow:
            for c in range(COLS):
                matrix[0][c] = 0
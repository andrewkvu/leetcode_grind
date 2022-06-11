class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        # reverse top -> bottom
        for i in range(rows // 2):
            for j in range(cols):
                temp = matrix[i][j]
                matrix[i][j] = matrix[rows - i - 1][j] # rows = 3, but want 0 indexed so -1
                matrix[rows - i - 1][j] = temp
        
        # then swap symmetrical indices
        for i in range(rows):
            for j in range(i + 1, cols):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
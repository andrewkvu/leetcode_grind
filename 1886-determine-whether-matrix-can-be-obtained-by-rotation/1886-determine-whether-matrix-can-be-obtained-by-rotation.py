class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        rows = len(mat)
        cols = len(mat[0])
        for i in range(4):
            self.rotate(mat, rows, cols)
            if mat == target:
                return True
        return False
            
    def rotate(self, matrix, rows, cols):
        for i in range(rows // 2):
            for j in range(cols):
                temp = matrix[i][j]
                matrix[i][j] = matrix[rows - i - 1][j]
                matrix[rows - i - 1][j] = temp
        
        for i in range(rows):
            for j in range(i + 1, cols):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                
                
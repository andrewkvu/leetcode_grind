class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        HEIGHT = len(matrix)
        WIDTH = len(matrix[0])

        left = 0
        right = WIDTH
        top = 0
        bottom = HEIGHT

        while left < right and top < bottom:
            # top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            # right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break

            # bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            # left col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res
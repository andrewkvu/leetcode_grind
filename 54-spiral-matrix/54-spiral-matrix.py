class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        up, left = 0, 0
        down, right = len(matrix) - 1, len(matrix[0]) - 1

        while True:
            # go from left to right
            for i in range(left, right + 1):
                res.append(matrix[up][i])
            up += 1
            if up > down:
                break
    #        print(res)

            # go from up to down
            for i in range(up, down + 1):
                res.append(matrix[i][right])
            right -= 1
            if left > right:
                break
    #        print(res)

            # go from right to left
            for i in range(right, left - 1, -1):
                res.append(matrix[down][i])
            down -= 1
            if up > down:
                break
    #        print(res)

            # go from down to up
            for i in range(down, up - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break
    #        print(res)

        return res
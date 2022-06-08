class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1. find which row target is in
        # 2. do the binary search in that row
        rows = len(matrix)
        cols = len(matrix[0])
        
        top, bottom = 0, rows - 1
        while top <= bottom:
            mid = top + (bottom - top) // 2
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][cols-1]:
                top = mid + 1
            else:
                break
        
        rowTarget = (top + bottom) // 2
        left, right = 0, cols - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if target == matrix[rowTarget][mid]:
                return True
            elif target < matrix[rowTarget][mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False
        
        
        
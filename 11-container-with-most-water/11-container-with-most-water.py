class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 2 pointers
        left, right = 0, len(height) - 1 # init at both ends since wide width is good
        res = 0

        while left < right:
            # width = right - left, height = minimum of left and right heights
            area = (right - left) * min(height[left], height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            res = max(res, area)

        return res
        
        
        
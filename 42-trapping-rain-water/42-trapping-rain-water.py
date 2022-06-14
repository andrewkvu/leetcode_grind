class Solution:
    def trap(self, height: List[int]) -> int:
        # 2 pointers
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right] # max so far
        res = 0
    
        while left < right:
            rain = 0
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                rain = maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                rain = maxRight - height[right]
            if rain > 0:
                res += rain
                
        return res
                
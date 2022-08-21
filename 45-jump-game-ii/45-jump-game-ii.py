class Solution:
    def jump(self, nums: List[int]) -> int:
        # somewhat two pointer/sliding window
        # have to check each value in the window to compute largest possible jump
        # adjust window accordingly and increment jumps
        
        left = right = minJumps = 0
        
        while right < len(nums) - 1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest
            minJumps += 1
        
        return minJumps
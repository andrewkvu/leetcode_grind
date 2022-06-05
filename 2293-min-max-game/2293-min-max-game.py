class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        
        newNums = []
        
        for i in range(0, n//2): # from 0 to n/2
            if i % 2 == 0:
                newNums.append(min(nums[2 * i], nums[2 * i + 1]))
            else:
                newNums.append(max(nums[2 * i], nums[2 * i + 1]))
                
        return self.minMaxGame(newNums)
        
        

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # keep track of the nondupe array index
        # keep scanning array until you find new number
        # when you find number, replace the value at the nondupe index with this 
        
        nondupe = 1
        
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[nondupe] = nums[i + 1]
                nondupe += 1
        
        return nondupe
                
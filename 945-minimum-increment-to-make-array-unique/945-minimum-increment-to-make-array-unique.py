class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        res = 0
        dupe = False
        N = len(nums)
        nums.sort()
        for i in range(N - 1):
            if nums[i] == nums[i + 1]:
                dupe = True
            
            if dupe and nums[i + 1] <= nums[i]: # if somehow the larger one gets smaller or equal than the smaller one
                res += 1 + nums[i] - nums[i + 1] # take the difference of the larger - smaller + 1
                # ie if 2 and 2, need to increase just by 1
                nums[i + 1] = nums[i] + 1 # then change the bigger one to the smaller one plus 1
            else:
                dupe = False
        
        return res
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False
        
        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                continue
            if changed:
                return False
            #    i, i+1
            #[3, 4, 2]
            # if i == 0, instantly runs so there isn't a runtime error
            if i == 0 or nums[i + 1] >= nums[i - 1]:
                nums[i] = nums[i + 1] # decrease nums[i]
            else:
                nums[i + 1] = nums[i] # increase nums[i + 1]
            changed = True
        
        return True
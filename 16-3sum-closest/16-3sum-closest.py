class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = sum([nums[0], nums[1], nums[2]])
        N = len(nums)
        nums.sort()
        
        for a in range(N - 2): # since 3sum
            # if a > 0 and nums[a] == nums[a - 1]: # duplicate?
            #     continue # don't need this because you can include duplicates
            left, right = a + 1, N - 1
            
            while left < right:
                threesum = sum([nums[a], nums[left], nums[right]])
                if threesum == target:
                    return threesum
                if abs(threesum - target) < abs(res - target): # clever way to check which ones closer to target
                    # in both a negative and positive case, still works
                    res = threesum
                if threesum < target:
                    left += 1
                else:
                    right -= 1
        
        return res
        
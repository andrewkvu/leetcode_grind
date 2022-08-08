class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        res = 0
        N = len(nums)
        c = Counter()
        totalPairs = (N * (N-1)) // 2
        # i < j
        # j - i != nums[j] - nums[i]
        # j - nums[j] != i - nums[i]
        # total pairs - good pairs
        for i, val in enumerate(nums):
            c[i - val] += 1
        
        for key, val in c.items():
            res += ((val * (val - 1)) // 2)
        
        return totalPairs - res
        
            
        
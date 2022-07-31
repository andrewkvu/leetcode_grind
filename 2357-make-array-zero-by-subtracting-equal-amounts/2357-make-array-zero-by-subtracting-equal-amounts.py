class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        different = set()
        for num in nums:
            if num != 0:
                different.add(num)
        
        return len(different)
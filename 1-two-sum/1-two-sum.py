class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  
        ansMap = {} # val : idx
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in ansMap:
                return [ansMap[diff], idx]
            ansMap[val] = idx # mapping original value to index to mark it down in the hashmap
        
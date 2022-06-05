class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        fmap = {}
        
#         for i in range(len(operations)):
#             fmap[operations[i][0]] = operations[i][1]
        
#         for i in range(len(nums)):
#             if nums[i] in fmap:
#                 nums[i] = fmap[nums[i]]
        
        for idx, val in enumerate(nums):
            fmap[val] = idx
        
        for op in operations:
            currVal = op[0]
            currIdx = fmap[currVal] # gives the index of the currVal
            nums[currIdx] = op[1]
            
            fmap.pop(currVal)
            fmap[nums[currIdx]] = currIdx
            
        return nums
        
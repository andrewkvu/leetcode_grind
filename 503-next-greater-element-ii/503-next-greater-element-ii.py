class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # initialize res array with -1's
        # stack with [index, nums[i]]
        # for each value, check if the stack is nonempty and check if this value 
        # is greater than the top element of the stack
        # while it is, keep popping from the stack and 
        # then set the position in res to that nums[i] value
        # do twice in order to get circular
        
        res = [-1] * len(nums)
        stack = [] # [index, value]
        
        for i in range(len(nums)):
            while stack and nums[i] > stack[-1][-1]:
                stackIndex, stackValue = stack.pop()
                res[stackIndex] = nums[i]
            stack.append([i, nums[i]])
            
        for i in range(len(nums)):
            while stack and nums[i] > stack[-1][-1]:
                stackIndex, stackValue = stack.pop()
                res[stackIndex] = nums[i]
            stack.append([i, nums[i]])
        
        return res
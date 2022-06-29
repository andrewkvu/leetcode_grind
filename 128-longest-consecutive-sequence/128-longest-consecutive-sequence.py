class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # check if the previous number is in the set
        
        seen = set(nums)
        globalLongest = 0
        
        for num in nums:
            # if the previous number isn't in the set, that means that it's the start of the sequence
            if num - 1 not in seen:
                length = 1 # thus length begins at 1
                while num + length in seen: # checks the sequence for each consecutive number in the set
                    length += 1
                globalLongest = max(length, globalLongest)
        
        return globalLongest
            
        
        
        
        
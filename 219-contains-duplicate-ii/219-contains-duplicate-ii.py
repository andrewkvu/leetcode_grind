class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        
        for idx, val in enumerate(nums):
            # by the time the next duplicate arrives, it checks if this value in the dictionary already
            # and if it is, if the index is <= k spaces away
            if val in dic and idx - dic[val] <= k: 
                return True
            dic[val] = idx # writes the dictionary by val, index
        return False
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        subset = []
        
        # i = index of nums where i = 0 is 1 for nums[1,2,3]
        def dfs(i):
            if i >= len(nums): # if i out of bounds/past the leaf node
                ans.append(subset.copy())
                return
            
            # case where include nums[i] in subset
            subset.append(nums[i])
            dfs(i + 1)
            
            # case where NOT include nums[i] in subset
            subset.pop()
            dfs(i + 1)
            
        # call with first index 0
        dfs(0)
        return ans
            
            
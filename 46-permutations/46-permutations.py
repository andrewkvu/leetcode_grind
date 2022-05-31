class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            
            # [2,3, 1], [3,2,1]
            for perm in perms:
                perm.append(n)
            res += perms
            nums.append(n)
        return res
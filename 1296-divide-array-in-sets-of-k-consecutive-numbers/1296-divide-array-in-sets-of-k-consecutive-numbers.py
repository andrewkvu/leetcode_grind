class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        nums.sort()
        have = Counter(nums)
        
        for num in nums:
            if have[num] > 0:
                need = have[num]
                for i in range(num, num + k):
                    if have[i] < need:
                        return False
                    have[i] -= need
        return True
    
            
            
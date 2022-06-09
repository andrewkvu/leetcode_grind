class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers
        # if sum is too big, move right pointer
        # if sum is too small, move left pointer
        
        left, right = 0, len(numbers)-1
        
        while left < right:
            msum = numbers[left] + numbers[right]
            if msum == target:
                return [left + 1, right + 1]
            elif msum < target:
                left += 1
            else:
                right -= 1
                
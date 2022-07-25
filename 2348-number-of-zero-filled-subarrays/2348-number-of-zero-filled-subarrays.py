class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # sliding window 2 pointers
        count = 0
        N = len(nums)
        left = right = 0

        while left < N and right < N:
            if nums[left] != 0:
                left += 1
                right += 1
            elif nums[left] == 0 and nums[right] == 0:
                while nums[right] == 0:
                    windowSize = 1 + right - left
                    count += windowSize
                    if right + 1 < N and nums[right + 1] == 0:
                        right += 1
                    else:
                        break
                right += 1
                left = right

        return count
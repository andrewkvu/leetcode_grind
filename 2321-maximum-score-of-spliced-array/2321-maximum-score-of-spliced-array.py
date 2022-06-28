class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        def kadane(A, B):
            currMaxDiff = currGlobalDiff = 0

            for i in range(len(A)):
                # calculates the max difference in "profit" you can get from swapping
                currMaxDiff = max(0, currMaxDiff + (A[i] - B[i])) 
                currGlobalDiff = max(currMaxDiff, currGlobalDiff)
            
            return currGlobalDiff + sum(B)
        return max(kadane(nums1, nums2), kadane(nums2, nums1))
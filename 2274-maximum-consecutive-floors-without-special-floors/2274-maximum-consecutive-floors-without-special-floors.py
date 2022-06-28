class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        # when sorted, first case: upper of special - lower of special
        # bottom - lower of special
        # top - upper of special
        # in between each special two pointer - 1
        special.sort()
        upper = special[-1]
        lower = special[0]
        ans = 0
        
        # case 1:
        ans = max(ans, lower - bottom)
        
        # case2:
        ans = max(ans, top - upper)
        
        # case3:
        for i in range(len(special) - 1):
            ans = max(ans, special[i + 1] - special[i] - 1)
        
        return ans
class Solution:
    def minPartitions(self, n: str) -> int:
        res = -1
        for char in n:
            res = max(res, int(char))
            
        return res
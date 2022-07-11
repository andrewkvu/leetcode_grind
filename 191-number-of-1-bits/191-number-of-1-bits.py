class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            res += n % 2 # want ones
            n = n >> 1 # shift bits to the right by one
        return res
            
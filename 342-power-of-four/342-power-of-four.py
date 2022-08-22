class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 1:
            if n % 4 == 0:
                n = n // 4
            else:
                return False
        return True if n == 1 else False
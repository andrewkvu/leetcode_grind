class Solution:
    def isHappy(self, n: int) -> bool:
        # cycle detection
        hset = set()
        
        while n != 1:
            msum = 0
            for digit in str(n):
                msum += int(digit) ** 2
            if msum in hset:
                return False
            n = msum
            hset.add(msum)
        
        return True
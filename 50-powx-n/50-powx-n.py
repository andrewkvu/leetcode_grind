class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0: return 1
            if x == 0 or x == 1: return x
            
            # n = 4 -> n = 2 -> n = 1
            # n = 5 -> n = 2 -> n = 1
            # x * x^2 * x^2 = x^5
            res = helper(x, n // 2)
            res *= res
            # multiply by x if exponent odd, else its normal
            return x * res if n % 2 == 1 else res
        
        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res
        # x^-n = 1 / x ^ n
        
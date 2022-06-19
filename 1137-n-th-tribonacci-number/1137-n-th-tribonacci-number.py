class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        f0 = 0
        f1 = 1
        f2 = 1
        
        for i in range(3, n + 1):
            fn = f0 + f1 + f2
            f0 = f1
            f1 = f2
            f2 = fn
        return f2
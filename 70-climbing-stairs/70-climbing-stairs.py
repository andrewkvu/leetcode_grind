class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        f1 = 1
        f2 = 2
        
        for i in range(3, n + 1):
            fn = f1 + f2
            f1 = f2
            f2 = fn
        
        return f2
        
        
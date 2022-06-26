class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        
        f0 = 1
        f1 = 2
        
        for i in range(2, n + 1):
            fn = f0 + f1
            f0 = f1
            f1 = fn
        
        return (f1 * f1) % MOD
        
        
        
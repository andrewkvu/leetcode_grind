class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return sorted(str(n)) in [sorted(str(1 << i)) for i in range(30)]
        powers = []
        for i in range(30):
            powers.append(sorted(str(1 << i)))
        
        return sorted(str(N)) in powers
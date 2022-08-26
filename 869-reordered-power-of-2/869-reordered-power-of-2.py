class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        powers = []
        for i in range(30):
            powers.append(sorted(str(1 << i)))
        
        return sorted(str(n)) in powers
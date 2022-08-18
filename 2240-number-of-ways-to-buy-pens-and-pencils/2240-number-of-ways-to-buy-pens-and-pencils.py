class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        if cost1 > total and cost2 > total:
            return 1
        
        res = 0
        n = total // cost1
        for i in range(n + 1):
            amtLeft = max(total - (cost1 * i), 0)
            res += (amtLeft // cost2) + 1
        
        return res
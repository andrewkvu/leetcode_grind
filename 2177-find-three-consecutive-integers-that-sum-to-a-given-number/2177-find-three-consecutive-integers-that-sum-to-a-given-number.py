class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # sum of three means that its only valid if num % 3 == 0
        if num % 3 != 0:
            return []
        
        res = []
        
        middle = num // 3
        res.append(middle - 1)
        res.append(middle)
        res.append(middle + 1)
        
        return res
        
        
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2: # if remainder is 2 ie 14, eventually goes to 2/3 which isnt a power 3
                return False
            n = n // 3
        
        return True
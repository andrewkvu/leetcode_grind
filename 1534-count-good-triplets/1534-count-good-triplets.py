class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    checkA = abs(arr[i] - arr[j])
                    checkB = abs(arr[j] - arr[k])
                    checkC = abs(arr[i] - arr[k])
                    if checkA <= a and checkB <= b and checkC <= c:
                        count += 1
                        
        return count
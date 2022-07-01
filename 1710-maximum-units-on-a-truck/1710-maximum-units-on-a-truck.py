class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # custom sort by the 1st index of each individual array
        # keep track of boxCount, index, sum
        boxTypes.sort(key = lambda x: (-x[1]))
        maxUnits = 0
        boxCount = 0
        i = 0
    
        lessCount = 0
        totalUnits = 0
        for arr in boxTypes:
            lessCount += arr[0]
            totalUnits += (arr[0] * arr[1])
        if lessCount < truckSize:
            return totalUnits
            
        
        while boxCount < truckSize:
            if boxTypes[i][0] > 0:
                maxUnits += boxTypes[i][1]
                boxTypes[i][0] -= 1
                boxCount += 1
            else:
                i += 1
        
        return maxUnits
            
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10 ** 9 + 7
        horizontalCuts.sort()
        verticalCuts.sort()
        
        maxHori = horizontalCuts[0]
        maxVert = verticalCuts[0]
        
        for i in range(len(horizontalCuts) - 1):
            maxHori = max(maxHori, horizontalCuts[i + 1] - horizontalCuts[i])
            
        for i in range(len(verticalCuts) - 1):
            maxVert = max(maxVert, verticalCuts[i + 1] - verticalCuts[i])
        
        maxHori = max(maxHori, h - horizontalCuts[-1])
        maxVert = max(maxVert, w - verticalCuts[-1])
        return (maxHori * maxVert) % MOD
            
        
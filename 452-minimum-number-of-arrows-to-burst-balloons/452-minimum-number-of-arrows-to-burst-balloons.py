class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = 1
        prevEnd = points[0][1]
        
        # if there are overlapping intervals, increase res and keep track of prevEnd
        for start, end in points[1: ]:
            if start > prevEnd:
                prevEnd = end
                res += 1
            else:
                prevEnd = min(prevEnd, end)
        
        return res
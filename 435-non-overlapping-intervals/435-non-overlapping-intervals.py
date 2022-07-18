class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        prevEnd = intervals[0][1]
        for start, end in intervals[1: ]:
            if start >= prevEnd: # since >= doesn't count as overlapping
                prevEnd = end # we move onto next interval
            else:
                res += 1
                prevEnd = min(prevEnd, end)
        
        return res
                
            
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda x: x[0]) # sort by the beginning of each interval
        
        for interval in intervals:
            # normal case: if res is empty or current end in res is less than beginning of curr interval
            if not res or res[-1][-1] < interval[0]:
                res.append(interval)
            else: # merge intervals
                res[-1][-1] = max(res[-1][-1], interval[-1])
        
        return res
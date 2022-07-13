class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # if the prevEnd, intervals[i][-1] >= intervals[i+1][0],
        # the new interval is intervals[i][0], intervals[i+1][-1]
        
        # where x is each individual array of 2
        intervals.sort(key = lambda x: (x[0]))
        res = []
        
        for interval in intervals:
            # if res is null or if the end of res's last element is less 
            # than this interval's beginning ([1, 2]) --> [3, 5] 
            # where 2 is res[-1][-1] and interval[0] = 3
            if not res or res[-1][-1] < interval[0]:
                res.append(interval)
            # ([1,4][2,5])
            else: # to merge, take max of the last element's end and current end and change res's ending
                res[-1][-1] = max(res[-1][-1], interval[-1])
        return res
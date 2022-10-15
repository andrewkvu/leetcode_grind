class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # make res array for output
        res = []
        # sort list of intervals by first
        intervals.sort(key = lambda x: x[0])
        # loop through each interval of the array
        for interval in intervals:
        # 2 cases:
        # case 1: new interval starts at a normal time - if its the first interval OR if this interval's beginning is after the last interval's end
            if not res or interval[0] > res[-1][-1]:
            # append interval
                res.append(interval)
        # case 2: new interval starts in between the previous interval's end time
            else:
                res[-1][-1] = max(res[-1][-1], interval[-1])
            # set the current last interval in the res array to the max of the current last interval's end
            # and the new interval's last end
            
        # then return result
        return res
        
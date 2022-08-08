class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        m, currDay = {}, 0
        for i, task in enumerate(tasks):
            currDay += 1
            # just a math equation 3->5 ---> increase by 2 days which is space + 1 - currDay - m[task]
            if task in m and currDay - m[task] < space + 1:
                currDay += (space + 1) - (currDay - m[task]) 
            m[task] = currDay
        return currDay
class MedianFinder:
    # 2 heaps
    # as long as abs(smallheap - largeheap) <= 1, its good
    # by default, always add to smallheap
    # check if max(smallheap) <= min(largeheap)
    # if not, move the max(smallheap) to the largeheap

    def __init__(self):
        # need medians which are closer to end of small and beg of large
        self.small = [] # max heap
        self.large = [] # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num) # negative for max heap, push small by default
        # make sure biggest val in small <= smallest val in large by checking opposite
        if self.small and self.large and (-1 * self.small[0] > self.large[0]): # 0th index is max/min, negative for small
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val) # push max from small into large if max from small > min
        # check for approximate size
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # odd number of elements = max or min of whatever has more elements
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
class KthLargest:

    # minHeap for K largest integers
    # keep popping the min from the heap until len of heap == k
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap) # converts the original minHeap (nums) into a heap
        # while len(self.minHeap) > k:
        #     heapq.heappop(self.minHeap)
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.k: 
            heapq.heappop(self.minHeap)

        # return minimum in the heap when len == k
        return self.minHeap[0] 
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[-k]
        
        # with heapq:
        # heap = []
        # for num in nums:
        #     heapq.heappush(heap, num)
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # # [3] [2,3] [1,3,2] [2,3] [2,3,5] [3,5] [3,5,6] [5,6] [4,6,5] [5,6]
        # return heap[0]
        
        heap = [-num for num in nums]
        heapq.heapify(heap)
        
        for i in range(k):
            ans = heapq.heappop(heap)
        
        return -ans
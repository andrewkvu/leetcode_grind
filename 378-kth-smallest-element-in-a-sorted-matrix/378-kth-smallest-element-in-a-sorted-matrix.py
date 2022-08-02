class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # kth smallest element from N sorted rows
        N = len(matrix)

        minHeap = [] # val, r, c
        for r in range(min(N, k)):
            heapq.heappush(minHeap, (matrix[r][0], r, 0))
            # pushing the first val of each row, and (r,c)

        val = float('inf')
        for i in range(k):
            val, r, c = heapq.heappop(minHeap)
            if c + 1 < N: # if next column is valid index
                # go through the next column and push, then repeat
                heapq.heappush(minHeap, (matrix[r][c + 1], r, c + 1))
        return val
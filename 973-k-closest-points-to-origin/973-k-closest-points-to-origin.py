class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for x, y in points:
            dist = math.sqrt((x ** 2) + (y ** 2)) # euclidean
            distances.append([dist, x, y])

        heapq.heapify(distances) # heapifies by the first value in the list (min distance)
        res = []

        for i in range(k): # get k closest distances
            dist, x, y = heapq.heappop(distances)
            res.append([x, y])
            
        return res
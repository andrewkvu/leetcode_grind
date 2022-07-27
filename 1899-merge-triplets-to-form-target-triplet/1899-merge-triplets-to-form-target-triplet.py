class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = set()
        for trip in triplets:
            # if any of the current triplets values are greater than the current targets,
            # we don't want to use it to max out, since it won't work
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                continue # skip iteration
            for i, val in enumerate(trip):
                if val == target[i]:
                    res.add(i) # has to be a set so that you can add indices without dupes
        
        return len(res) == 3
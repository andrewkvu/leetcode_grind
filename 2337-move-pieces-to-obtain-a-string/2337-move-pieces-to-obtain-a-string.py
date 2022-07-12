class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace("_", "") != target.replace("_", ""): # checking if they're even able to be moved in the right positions
            return False # which is the start[i] != target[i] thing
        i = j = 0 # i is start index, j is target index
        N = len(start)

        while i < N and j < N:
            # finding the first L/R in the start and target
            while i < N and start[i] == '_':
                i += 1
            while j < N and target[j] == '_':
                j += 1

            if i < N and j < N:
                if start[i] == 'L' and j > i: # checking if the target L is after the start L which is impossible
                    return False
                if start[i] == 'R' and i > j: # checking if the target R is before the start R which is impossible
                    return False
            i += 1
            j += 1

        return True
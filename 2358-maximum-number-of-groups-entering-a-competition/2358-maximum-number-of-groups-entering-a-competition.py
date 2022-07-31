class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        N = len(grades)
        groups = 0
        
        while N >= groups + 1:
            groups += 1
            N -= groups
        
        return groups
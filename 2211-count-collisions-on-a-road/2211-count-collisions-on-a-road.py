class Solution:
    def countCollisions(self, directions: str) -> int:
        left, right = 0 , len(directions) - 1
        
        while left < len(directions) and directions[left] == 'L':
            left += 1
        
        while right >= 0 and directions[right] == 'R':
            right -= 1
        
        collisions = 0
        for i in range(left, right + 1):
            if directions[i] != 'S': # only moving cars cause collisions
                collisions += 1
        
        return collisions
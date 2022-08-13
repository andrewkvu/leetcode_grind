class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res, left = 0, 0
        fruitCount = Counter()
        
        for right in range(len(fruits)):
            fruitCount[fruits[right]] += 1
            if len(fruitCount) > 2:
                fruitCount[fruits[left]] -= 1
                if fruitCount[fruits[left]] == 0:
                    fruitCount.pop(fruits[left])
                left += 1
            
            res = max(res, 1 + right - left)
        
        return res
            
                
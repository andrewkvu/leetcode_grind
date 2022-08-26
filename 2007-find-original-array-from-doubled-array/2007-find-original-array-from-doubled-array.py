class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count = Counter(changed)
        s = sorted(changed)
        res = []
        if count[0] % 2 == 1:
            return []
        # 1,2,3,4,6,8
        for num in s:
            if count[num] == 0:
                continue
            if count[num * 2] == 0:
                return []
            res.append(num)
            count[num] -= 1
            count[num * 2] -= 1
        
        return res
        
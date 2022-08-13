class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        c1 = Counter(s1)
        c2 = Counter()

        left = 0

        for right in range(len(s2)):
            c2[s2[right]] += 1
            if (1 + right - left) < sum(c1.values()):
                continue
            if c1 == c2:
                return True
            c2[s2[left]] -= 1
            if c2[s2[left]] == 0:
                c2.pop(s2[left])
            left += 1

        return False
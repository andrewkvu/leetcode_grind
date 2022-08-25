class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)
        
        for key, val in r.items():
            if key not in m or val > m[key]:
                return False
        
        return True
            
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sc = Counter()
        pc = Counter(p)

        ans, left = [], 0

        for right in range(len(s)):
            sc[s[right]] += 1 # add until window size is correct
            if (1 + right - left) < sum(pc.values()):
                continue
            if sc == pc: # append answer when anagram
                ans.append(left)
            sc[s[left]] -= 1 # remove left part of window
            if sc[s[left]] == 0:
                sc.pop(s[left]) # remove characters with no value anymore
            left += 1 # shift window

        return ans
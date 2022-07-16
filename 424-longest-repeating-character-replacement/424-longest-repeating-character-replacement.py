class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        count = Counter()
        res = left = 0
        for right in range(len(s)):
            count[s[right]] += 1
            # if windowsize - max value of the hashmap <= k?:
            # lowest window size is 1
            if (1 + right - left) - max(count.values()) <= k:
                res = max(res, 1 + right - left)
            else:
                count[s[left]] -= 1 # decrement count of hashmap at left since its out of the sliding window now
                left += 1 
        return res
            
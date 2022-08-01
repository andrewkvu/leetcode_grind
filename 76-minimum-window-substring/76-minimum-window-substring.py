class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        dt, window = Counter(t), Counter()
        have, need = 0, len(dt) # want unique characters from t
        res, resLen = [-1, -1], float('inf') # res = [l, r]
        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] += 1

            if char in dt and window[char] == dt[char]: # good character from t is in current window
                have += 1
            
            # case where we actually have the right chars
            while have == need: # update our result
                if (1 + r - l) < resLen:
                    res = [l, r]
                    resLen = (1 + r - l)
                # removing from the left case
                window[s[l]] -= 1 # pop left from window, try to minimize windowsize
                if s[l] in dt and window[s[l]] < dt[s[l]]: # if this char was an important char to t and as a result
                    have -= 1 # the windowMap val is less than the t map, meaning have is decremented
                l += 1

        l, r = res
        return s[l:r + 1] if resLen != float('inf') else ""
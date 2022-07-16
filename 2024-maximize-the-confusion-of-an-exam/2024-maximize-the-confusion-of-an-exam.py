class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count = Counter()
        
        res = left = 0
        
        for right in range(len(answerKey)):
            count[answerKey[right]] += 1
            if (1 + right - left) - max(count.values()) <= k:
                # res = max(res, 1 + right - left) # also just += 1
                res += 1
            else:
                count[answerKey[left]] -= 1
                left += 1
                
        return res
            
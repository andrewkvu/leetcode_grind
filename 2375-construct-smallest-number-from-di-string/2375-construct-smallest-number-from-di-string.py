class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # res length is len(pattern) + 1
        res = [1]
        ans = ""
        
        for char in pattern:
            if char == 'I': # append the lowest increased number possible that isn't in res
                num = res[-1] + 1
                while num in res:
                    num += 1
                res.append(num)
            else: 
                res.append(res[-1]) # use res[-1] as placeholder for new element
                for i in range(len(res) - 1, 0, -1): # reverse from end to 0
                    if res[i - 1] == res[i]: # add one to current 2nd to last element
                        res[i - 1] += 1 # if they are the same which they should be
        
        for num in res:
            ans += str(num)
        
        return ans
                
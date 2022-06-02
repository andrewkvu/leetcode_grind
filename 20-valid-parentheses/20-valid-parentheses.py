class Solution:
    def isValid(self, s: str) -> bool:
        parMap = {'}': '{', ')': '(', ']': '['}
        stack = []
        for char in s:
            if char in parMap: # if the char is a closing par
                # check if stack is empty or if the last char is an opening par
                if stack == [] or parMap[char] != stack.pop():
                    return False
            else: # if the char is an opening par
                stack.append(char)
        
        # return len(stack) == 0
        return not stack
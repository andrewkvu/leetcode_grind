class Solution:
    def isValid(self, s: str) -> bool:
        # for each char in the string
        # if the char is open parenthesis, append
        # if char is closed, check if this is a closed parenthesis and the top is an open one, blah blah
        
        stack = []
        
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if (top == '(' and char != ')') or (top == '[' and char != ']') or (top == '{' and char != '}'):
                    return False
                
        return not stack
        
        # return whether stack is empty or not
        # true is stack is empty
        
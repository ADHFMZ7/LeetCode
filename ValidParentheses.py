class Solution:
    def isValid(self, s: str) -> bool:
        d = {']' : '[', '}' : '{', ')' : '(' }
        stack = []

        for i in s:
            if i in [')', ']', '}']:
                if len(stack) < 1 or d[i] != stack[-1]:
                    return False
                stack.pop()

            else: 
                stack.append(i)
        return len(stack) == 0
        

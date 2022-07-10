operators = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : truediv
}

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in ['+', '-', '/', '*']:
                stack.append(int(operators[tokens[i]](stack.pop(len(stack)-2), stack.pop())))
            else:
                stack.append(int(tokens[i]))
        return stack[0]

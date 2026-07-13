import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_map = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b)
        }
        stack = []
        
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                op = op_map[token]
                print(a,token, b)
                stack.append(op(b, a))
        
        return stack[-1]

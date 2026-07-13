class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                x = ""
                match c:
                    case ")":
                        x = "("
                    case "}":
                        x = "{"
                    case "]":
                        x = "["
                
                if not stack or stack[-1] != x:
                    return False
                else:
                    stack.pop()
        
        if stack:
            return False
        
        return True

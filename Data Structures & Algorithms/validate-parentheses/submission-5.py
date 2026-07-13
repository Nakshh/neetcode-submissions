class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        for c in s:
            if c in "({[":
                stack.append(pairs[c])
            else:                
                if not stack or stack[-1] != c:
                    return False
                else:
                    stack.pop()
        
        if stack:
            return False
        
        return True

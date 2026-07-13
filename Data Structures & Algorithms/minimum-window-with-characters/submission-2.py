from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        right = 0
        answer = ""

        if len(t) > len(s):
            return ""

        for i, c in enumerate(s):
            if c in t:
                right = i + len(t)
                print(right)
                while right <= len(s):
                    if Counter(t) <= Counter(s[i:right]):
                        print("brudda man")
                        answer = s[i:right] if answer == "" or len(s[i:right]) < len(answer) else answer
                        break
                    else:
                        right += 1
                    

        return answer
                
                        

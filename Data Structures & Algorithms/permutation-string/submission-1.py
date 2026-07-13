from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cs1 = Counter(s1)
        
        for i in range(len(s2)-len(s1)+1):
            if cs1 <= Counter(s2[i:i+len(s1)]):
                return True

        return False
        
            

        
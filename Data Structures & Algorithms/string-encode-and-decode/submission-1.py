from collections import deque

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for s in strs:
            encoded_string += str(len(s)) + "#" + s

        return encoded_string
        
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        q = deque(s)
        
        while q:

            n = ""
            while q[0] != "#":
                n += q.popleft()
            q.popleft()
            n = int(n)
            d = ""
            for i in range(n):
                d += q.popleft()
            decoded_strs.append(d)

        
        return decoded_strs

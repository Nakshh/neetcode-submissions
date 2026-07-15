class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = sorted([nums1, nums2], key=len)
        half = (len(A) + len(B)) // 2
        odd = (len(A) + len(B)) % 2

        l = 0
        r = len(A)
        while l <= r:
            midA = (l + r) // 2
            midB = half - midA
            leftA = float("-inf") if midA == 0 else A[midA - 1]
            rightA = float("inf") if midA == len(A) else A[midA]

            leftB = float("-inf") if midB == 0 else B[midB - 1]
            rightB = float("inf") if midB == len(B) else B[midB]

            if leftA > rightB:
                r = midA - 1
            elif leftB > rightA:
                l = midA + 1
            else:
                if odd:
                    return min(rightA, rightB)
                return (max(leftA, leftB) + min(rightA, rightB)) / 2

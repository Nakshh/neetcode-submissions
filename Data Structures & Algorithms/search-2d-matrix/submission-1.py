class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lh = 0
        rh = len(matrix)

        while lh < rh:
            mid = (lh+rh) // 2        
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                l = 0
                r = len(matrix[mid])
                while l<r:
                    middle = (l+r) // 2
                    if matrix[mid][middle] == target:
                        return True
                    elif matrix[mid][middle] > target:
                        r = middle
                    else:
                        l = middle+1
                return False
            elif matrix[mid][0] > target:
                rh = mid
            else:
                lh = mid + 1
            
        return False
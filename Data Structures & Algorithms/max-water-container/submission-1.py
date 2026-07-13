class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        ans = 0
        while left < right:
            area = (right-left) * min(heights[right], heights[left])
            ans = max(area, ans)

            if heights[right] <= heights[left]:
                right -= 1
            else:
                left += 1
        
        return ans

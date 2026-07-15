class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            n = abs(num)
            if nums[n] < 0:
                return n
            else:
                nums[n] *= -1
        
        

        
        
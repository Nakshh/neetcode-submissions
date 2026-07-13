class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        
        p = 1
        for i, num in enumerate(nums):
            prefix[i] = p
            p *= num
        
        s = 1
        for j in range(len(nums) - 1, -1, -1):
            suffix[j] = s
            s *= nums[j]

        return [a * b for a, b in zip(prefix, suffix)]
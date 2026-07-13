class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 0
        
        nums = set(nums)
        ans = []
        for num in nums:
            a = 1
            if num-1 not in nums:
                n = num
                while n+1 in nums:
                    a += 1
                    n+=1
                ans.append(a)
        
        return max(ans)
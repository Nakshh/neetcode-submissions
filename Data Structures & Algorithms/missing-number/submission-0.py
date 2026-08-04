from functools import reduce
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums += [i for i in range(n+1)]
        return reduce(lambda x, y: x^y, nums)
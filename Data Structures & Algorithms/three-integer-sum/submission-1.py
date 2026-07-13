class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()

        for j in range(len(nums)):
            d = set()
            target = -nums[j]

            for i in range(len(nums)):
                if i == j:
                    continue

                complement = target - nums[i]

                if complement in d:
                    result.add(tuple(sorted([nums[j], complement, nums[i]])))

                d.add(nums[i])

        return [list(triplet) for triplet in result]
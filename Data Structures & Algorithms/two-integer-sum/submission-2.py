class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}

        for idx, num in enumerate(nums):
            comp = target - num
            if comp in x:
                return [x[comp], idx]
            else:
                x[num] = idx
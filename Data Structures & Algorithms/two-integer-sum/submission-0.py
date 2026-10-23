class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}

        for index, num in enumerate(nums):
            goal = target - num
            if goal in x:
                return [x[goal], index]
            x[num] = index
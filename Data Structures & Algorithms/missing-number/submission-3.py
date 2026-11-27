class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = sum(range(len(nums) + 1))
        b = sum(nums)
        return a - b

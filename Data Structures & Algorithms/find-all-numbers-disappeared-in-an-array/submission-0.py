class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        snums = set(nums)
        res = []
        for i in range(1,len(nums)+1):
            if i not in snums:
                res.append(i)

        return res
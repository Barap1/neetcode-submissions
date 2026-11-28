class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        l = prices[0]

        for p in prices:
            if p < l:
                l = p
            if p - l > mp:
                mp = p - l

        return mp


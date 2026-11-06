class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        l = 0
        for r in range(len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r]-prices[l]
                mp = max(mp, profit)
            else:
                l = r
        return mp

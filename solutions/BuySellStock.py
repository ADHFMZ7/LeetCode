class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s, t = 0, 0, 0
        for i, p in enumerate(prices):
            if p - prices[b] < 0:
                b, s = i, i
            elif p - prices[b] > t:
                s = i
            t = max(t, prices[s] - prices[b])
            
        return t

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0 
        for i in range(len(prices) - 1):
            l = i + 1
            while l < len(prices):
                total = prices[l] - prices[i]
                res = max(total, res)
                l += 1
        return res
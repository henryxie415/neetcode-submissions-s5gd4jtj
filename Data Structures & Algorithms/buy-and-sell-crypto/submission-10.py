class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #use two pointers 
        profit = 0
        

        for i in range(len(prices) - 1):
            r = i + 1
            while r < len(prices):
                if prices[i] < prices[r]:
                    total = prices[r] - prices[i]
                    profit = max(total, profit)
                r += 1
        return profit
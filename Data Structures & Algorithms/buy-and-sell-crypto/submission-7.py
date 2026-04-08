class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #position matters
        #when looking through the list if you need to look left and right, use two pointers 
        #find the lowest number and the number to its righ to be the max
        #once lowest number is set find the first index of it and then find max 
        #if lowest is at the end set zero 
        #two pointers

        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l=r
            r += 1
        return maxP    





        
        
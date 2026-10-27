import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        res = r 

        while l <= r:
            m = (l + r) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(float(pile)/m)

                #whoever has the biggest hours 
            if hours <= h:
                res = m
                r = m - 1
            else:
                l = m + 1

        return res 

        #find the lowest rate which is the lowest pile 
        #find the highest rate which is the highest pile
        #binary search the rate to find the minimum
        #with the rate you divide the piles by the rate and roundup to add them up 
        #the closest to the hour or at the hour means the minimum rate 
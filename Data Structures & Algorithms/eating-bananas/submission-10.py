import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = 0
        while l <= r:
            hours = 0
            for pile in piles:
                m = (l+r)// 2
                hours += math.ceil(pile / m)

            if hours <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
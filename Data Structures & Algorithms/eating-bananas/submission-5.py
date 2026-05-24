class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #use the max pile to find the max rate 
        l = 1
        r = max(piles)
        res = r

        while l <= r:

            m = (l + r) // 2
            totalTime = 0

            for pile in piles:
                totalTime += math.ceil(float(pile) / m)

            if totalTime <= h:
                res = m
                r = m - 1

            else:
                l = m + 1

        return res 

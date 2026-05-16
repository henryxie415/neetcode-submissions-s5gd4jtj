class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #go through the piles and see which is the largest 
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            m = (l + r) // 2
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile)/m)
            if h >= totalTime:
                r = m - 1
                res = m
            else:
                l = m + 1
        return res 
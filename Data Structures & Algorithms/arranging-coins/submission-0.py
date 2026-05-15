class Solution:
    def arrangeCoins(self, n: int) -> int:

        #for each staircase it goes with the ith row,
        #have it stop once n runs out by having it be subtracted from n
        rows = 0
        l = 0
        r = n
        while r > 0:
            l += 1
            r = r - l
            if r < 0:
                break
            rows += 1
        return rows
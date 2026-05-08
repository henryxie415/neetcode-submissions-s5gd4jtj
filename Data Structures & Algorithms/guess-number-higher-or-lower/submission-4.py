# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #create the bounds of search 
        l = 0
        r = n

        #create the loop in for the guess game 
        while True:
            m = (l + r) // 2
            #the guess function tells if right or wrong
            #mid point is the constant search update
            res = guess(m)
            if res < 0:
                r = m - 1
            elif res > 0:
                l = m + 1
            else:
                return m


    
class Solution:
    def validPalindrome(self, s: str) -> bool:
        #have a function determine if something is a palindrome
        def checker (l,r) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True 
        #go through the string: if deleted try to detect palindrome 
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return (checker(l+1, r) or checker(l,r-1))
            l += 1
            r -= 1
        return True

            

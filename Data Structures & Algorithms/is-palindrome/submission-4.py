class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join([c.lower() for c in s if c.isalnum()])
        x = 0
        for i in range(0,int(len(s)/2)):
            if s[i] != s[len(s) - 1 - x]:
                return False
            x += 1
        return True

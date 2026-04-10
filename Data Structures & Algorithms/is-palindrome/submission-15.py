class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""
        for c in s:
            if c.isalnum():
                d= c.lower()
                filtered += d

        l = 0
        r = len(filtered) - 1

        while l < r:
            if filtered[l] == filtered[r]:
                l += 1
                r -= 1
            else:
                return False

        return True
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0 
        r = len(s) - 1
        x = 0
        while l < r:
            x = s[l]
            s[l] = s[r]
            s[r] = x
            l += 1
            r -= 1

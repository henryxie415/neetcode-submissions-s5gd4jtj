class Solution:
    def scoreOfString(self, s: str) -> int:
        #loop through the string 
        total = 0
        for i in range(0,len(s)-1):
            final = abs(ord(s[i]) - ord(s[i+1]))
            total = total + final
        return total



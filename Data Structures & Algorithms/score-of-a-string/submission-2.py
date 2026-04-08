class Solution:
    def scoreOfString(self, s: str) -> int:
        #loop through the string 
        total = 0
        for i in range(0,len(s)-1):
            total += abs(ord(s[i]) - ord(s[i+1]))
        return total



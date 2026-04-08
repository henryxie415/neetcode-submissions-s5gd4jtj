class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        #two pointers
        #go through and compare the strings
        l = r = 0
        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                #keep track of the s and t
                l += 1
                r += 1
            else:
                #s is longer than t so goes through the entire s word 
                l += 1
        #r keeps track of how many same letters in succession
        return len(t) - r
        

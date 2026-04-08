class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       #add the asci value of s and t 
        #if they match then outpiut true else false
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        


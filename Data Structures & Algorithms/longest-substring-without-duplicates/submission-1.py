class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #keep the letters in the string in a hashmap
        charSet = []
        res = 0
        #sliding window keeps track of the length of the window
        l = 0 
        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[l])
                l += 1
            #starts with first character
            charSet.append(s[i])
            total = len(charSet)
            res = max(total, res)
        return res

            
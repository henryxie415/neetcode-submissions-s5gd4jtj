class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #create the pointer to go through the string
        l = 0

        #create the set to keep non repeating chars 
        keeper = set()

        #create the result variable to hold the max length of set
        res = 0

        for i in range(len(s)):
            while s[i] in keeper:
                keeper.remove(s[l])
                l += 1
            keeper.add(s[i])
            res = max(res, i - l + 1)
        return res





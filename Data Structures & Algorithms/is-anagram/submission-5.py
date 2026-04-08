class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #hash map to record number of letters 
        if len(s)!=len(t):
            return False 
        #hash table with arrays 
        map = [0] * 26
        #create a hash table to record the frequency of letters 

        count = {}

        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1


        for key in count:
            if count[key] != 0:
                return False

        return True

        #with 26 spaces for each letter
        #then add one for first word
        #subtract one for the other word
        #if they are anagrams then they hash table will be empty
        #if empty return True and if not return False 
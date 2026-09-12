class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1 = {}
        counter2 = {}

        for char in s:
            counter1[char] = counter1.get(char, 0) + 1
        for char in t:
            counter2[char] = counter2.get(char,0) + 1
        if counter1 == counter2:
            return True
        return False 

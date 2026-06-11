class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #go through s2 with the window being length of s1
        #sort the window of s2 and if its equal to s1 return True 
        #otherwise false 

        l = len(s1)
        keeper = {}
        sleeper = {}

        if len(s1) > len(s2):
            return False
        #goes through s2
        for i in range(len(s1)):
            keeper[s1[i]] = keeper.get(s1[i], 0) + 1
        print(keeper)

        for i in range(len(s2)):
            sleeper[s2[i]] = sleeper.get(s2[i], 0) + 1
            if i >= len(s1):
                left_char = s2[i - len(s1)]
                sleeper[left_char] -= 1
                if sleeper[left_char] == 0:
                    del sleeper [left_char]
            if sleeper == keeper:
                return True
        return False



            

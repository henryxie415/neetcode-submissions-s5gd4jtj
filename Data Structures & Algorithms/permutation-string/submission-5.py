class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #create a hashmap to look at the first string
        keeper = {}
        for i in range(len(s1)):
            keeper[s1[i]] = keeper.get(s1[i], 0) + 1
        print(keeper)

        #create the for loop to go through and add the characters from the second string 
        sleeper = {}
        for i in range(len(s2)):
            sleeper[s2[i]] = sleeper.get(s2[i], 0) + 1

            #if i > len(s1): (this makes it so once the window is full you can start deleting stuff)
            if i >= len(s1):
                left_char = s2[i - len(s1)]
                sleeper[left_char] -= 1
                #minus the left char by 1 in the frequency hashmap 
                if sleeper[left_char] == 0:
                    del sleeper[left_char] 
            if sleeper == keeper:
                return True
        return False 
        #Condition for victory: if you compare all keys and freqs and they are the same

        #sliding window: add char to map, delete char on the left side if 0

        



            

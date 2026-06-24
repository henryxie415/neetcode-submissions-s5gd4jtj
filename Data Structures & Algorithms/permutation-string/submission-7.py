class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        keeper = {}
        for i in range(len(s1)):
            keeper[s1[i]] = keeper.get(s1[i], 0) + 1


        sleeper = {}
        for i in range(len(s2)):
            sleeper[s2[i]] = sleeper.get(s2[i], 0) + 1
            #establish what the left char is going to be and how its going to be evicted from the hashmap 
            
            if i >= len(s1):
                left_char = s2[i - len(s1)]
                #condition is that if left_char not in sleeper we reduce it to zero
                sleeper[left_char] -= 1
                if sleeper[left_char] == 0:
                    del sleeper[left_char]

            #if there is a zero in the hashmap we delete the key 
            if keeper == sleeper:
                return True
        return False


        #now that we have two strings in two hash maps 
        #we need to add each letter in s2
        #and continually check the hashmap to see if its the same
        #the goal is to have 
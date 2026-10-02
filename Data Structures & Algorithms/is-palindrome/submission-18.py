class Solution:
    def isPalindrome(self, s: str) -> bool:
        #isolate the string with only alphanumerics 
        #get rid of all white spaces and store in variable
        #use a list and add to list halfway 
        #pop from list if letter already in there if not then add
        #if list empty return True else False 
        new_word = ''.join(c.lower() for c in s if c.isalnum())
        print(new_word)
        counter = []
        for i in range(0, len(new_word)//2):
            counter.append(new_word[i])
        
        print(counter)

        for i in range((len(new_word) + 1)//2, len(new_word)):
            if new_word[i] in counter:
                counter.remove(new_word[i])
            else:
                counter.append(new_word[i])
        
        if not counter:
            return True 
        return False 

class Solution:

    def encode(self, strs: List[str]) -> str:
        #encode you put the length and the pound sign in front on the word
        res = ''
        for word in strs:
            res += str(len(word)) + '#' + word
        return res 

    def decode(self, s: str) -> List[str]:
        #to decode you have the length of the word
        #you have the special character in front of the word
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j+ 1: j + 1 + length])
            i = j + 1 + length
        return res 
            



        #use two pointer to go through each word 
        #and place them in to a list 
        #have the first pointer move to the next word after the first word is done 

    










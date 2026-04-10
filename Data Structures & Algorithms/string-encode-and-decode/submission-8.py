class Solution:

    def encode(self, strs: List[str]) -> str:
        #start off by using length encoding
        word = ''
        for char in strs:
            word += str(len(char)) + '#' + char
        return word

    def decode(self, s: str) -> List[str]:
        #need array for the final output
        arr = []
        #need pointer to go through the entire string
        i = 0
        #need variable to hold the length of each string
        #need variable to hold the string value to convert to int and then reset after first word
        digit = ''

        while i < len(s):
            if s[i] != '#':
                digit += s[i]
                print(digit)
                i += 1
            else:
                j = int(digit)
                arr.append(s[i + 1 : i + j + 1])
                i += j + 1
                digit = ''
        return arr





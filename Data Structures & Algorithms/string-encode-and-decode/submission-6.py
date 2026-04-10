class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for char in strs:
            result += str(len(char))+'#'+char

        return result

    def decode(self, s: str) -> List[str]:
        #analyze the string

        strs = []
        i = 0
        digit = ''
        while i < len(s):
            if s[i] != '#':
                digit += s[i]
                i += 1
            else:
                l = int(digit)
                strs.append(s[i+1: i + l + 1])
                digit = ''
                i += l + 1
        return strs
        #the length is the first part
        #maybe use length as the delimiter








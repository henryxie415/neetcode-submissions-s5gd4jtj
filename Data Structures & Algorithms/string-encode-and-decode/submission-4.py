class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        if not strs:
            return ""
        for char in strs:
            result += str(len(char))+"#"+char
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        #analyze the string

        arr = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            arr.append(s[i:j])
            i = j
        return arr
        #the length is the first part
        #maybe use length as the delimiter








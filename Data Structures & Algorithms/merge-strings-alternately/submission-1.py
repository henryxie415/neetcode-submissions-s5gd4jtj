class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r = 0
        word = []
        while l < len(word1) or r < len(word2):
            if l < len(word1):
                word.append(word1[l])
                print(word)
                l += 1
                print(l)

            if r < len(word2):
                word.append(word2[r])
                print(word)
                r += 1
                print(r)
        return ''.join(word)
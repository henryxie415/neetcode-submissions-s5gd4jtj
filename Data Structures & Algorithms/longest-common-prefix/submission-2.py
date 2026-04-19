class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        map = {}
        n = len(strs[0])
        longest = max(strs, key=len)
        tmp = n
        first = strs[0]
        #build the hashmap with the index
        for i, value in enumerate(longest):
            map[i] = value
        print(map)
        #go through the next words and remember the lowest 
        for word in strs:
            counter = 0
            for i, value in enumerate(word):
                if value == map[i]:
                    counter += 1
                else:
                    break
            tmp = min(counter, tmp)
        return first[:tmp] 
            
        #if lowest is 0 return empty string
        #if higher than 0 return the first letters of the lowest number

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            #sort the words to make them all anagrams the same
            sorted_word = sorted(word)
            #join them together so that they make back one string
            final_word = ''.join(sorted_word)

            #if the word is not in the map, create a new key
            if final_word not in map:
                map[final_word] = [word]
            #else add the word into the list 
            else:
                map[final_word].append(word)
            #return the values of the dictionary but unsorted 
        return list(map.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a hash map for the anagrams 
        map = {}
    
        for word in strs:
            sorted_word = sorted(word)
            final_word = ''.join(sorted_word)
            if final_word not in map:
                map[final_word] = [word]
            else:
                map[final_word].append(word)
        print(map)

        return list(map.values())
        #attach the final word as the key and a list of strings as the value 

        #create an array to store the count 

        #create a for the final list

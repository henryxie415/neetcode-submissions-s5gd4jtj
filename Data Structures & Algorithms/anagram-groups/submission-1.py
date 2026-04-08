class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        #create the hashmap 
        for word in strs:
            sorted_word = sorted(word)
            final_word = ''.join(sorted_word)
            if final_word not in map:
                map[final_word] = [word]
            else:
                map[final_word].append(word)
        return list(map.values())
            
        #sort and join the words so that it will be the key
        #The value will be a list of the original words 


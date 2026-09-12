class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a hash map for the anagrams 
        counter = {} 
        res = []
        #sort the words and use the sorted word as the key 
        for i in range(len(strs)):
            new = sorted(strs[i])
            new = ''.join(new)
            if new not in counter:
                counter[new] = [strs[i]]
            else:
                counter[new].append(strs[i])
        return list(counter.values())
            
    #add the words into the map to make a list if it matches the sorted key
        #if key is not in the hashmap create a new list for it

        #go through the hashmap to put the final res into a master list


            

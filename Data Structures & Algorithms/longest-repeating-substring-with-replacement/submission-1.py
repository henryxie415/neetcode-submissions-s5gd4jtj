class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        char_counts = {}  # Our hash map to track frequencies
        l = 0
        max_repeat_count = 0
        res = 0

        for r in range(len(s)):
            # 1. Add the incoming character to the hash map
            char_counts[s[r]] = char_counts.get(s[r], 0) + 1
            
            # 2. Update the count of the most frequent character in the current window
            max_repeat_count = max(max_repeat_count,char_counts[s[r]]) 
            # 3. Isolate the impostors! If they exceed k, shrink from the left
            while (r - l + 1) - max_repeat_count > k:
                char_counts[s[l]] -= 1
                l += 1
                
            # 4. Calculate the max valid window size seen so far
            res = max(res, r - l + 1)
            
        return res



        #for each object in the keeper keeps count of consecutive letter 
        #if reaches a different letter and the k > 0 then the counter reset
        #keeps the max number for the object

        




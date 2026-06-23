class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        keeper = set(s) 
        # set to keep track of the unique characters 
        total = 1
        #goes through the unique characters 
        for char in keeper:
            l = 0
            count = 0
            tempCount = k
            #goes through the entire string to find the max count 
            for i in range(len(s)):
                if s[i] == char:
                    count += 1
                while (i - l + 1) - count > tempCount:
                    if s[l] == char:
                        count -= 1
                    l += 1


                total = max(i - l + 1, total)
        return total


        




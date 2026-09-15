class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #use a set to get rid of duplicates
        new = set(nums)
        count = 0
        #for anything that is the start of the sequence check if theres a number - 1 
        for number in nums:
            
            if (number - 1) not in new:
                length = 1
                #use the number and keep adding 1 to it
                #if in set then add on to the count
                while (number + length) in new:
                    length += 1
                count = max(length, count) 
        #if not thats the start and then keep adding 1 and keep checking if in the set
        #keep track of length with max 
        return count
        #return the final max 
        

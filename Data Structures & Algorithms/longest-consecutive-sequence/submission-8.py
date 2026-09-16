class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #use the set to get rid of duplicates 
        new = set(nums)
        counter = 0
        #use length to keep track of how many are in the consecutive 
        for num in nums:
            length = 1
            if (num - 1) not in new:
                while (num + length) in new:
                    length += 1
            counter = max(counter, length)
        return counter
        #if there is anything left of the number then it is the start of the series
        #keep adding 1 until theres nothing left
        #use counter to keep track of the max
        #return counter
        

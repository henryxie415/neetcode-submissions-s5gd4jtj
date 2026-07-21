class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #use a hashmap to count based on the linked list 
        container = {}

        #use a while loop to go through and map the counts 
        for num in nums:
            container[num] = container.get(num, 0) + 1
            if container[num] > 1:
                return num
        
        #if the counts is more than 1 then return that key  

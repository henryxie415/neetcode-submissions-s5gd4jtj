class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #target minus one number must be present 
        #if present add the two indices in the list 
        #Make a hash table with the llist then a for loop 
        #to lookup if in the hash table
        map = {}

        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in map:
                return [map[diff], i]
            map[num] = i

                    
                
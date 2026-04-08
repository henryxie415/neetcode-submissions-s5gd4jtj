class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #target minus one number must be present 
        #if present add the two indices in the list 
        #Make a hash table with the llist then a for loop 
        #to lookup if in the hash table
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i
        
        for i, value in enumerate(nums):
            diff = target - value 
            if diff in map and map[diff] != i:
                return [i, map[diff]]
        return []

                    
                
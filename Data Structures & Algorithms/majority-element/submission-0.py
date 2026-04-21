class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #create a hashmap and map out frequency 
        #frequencies higher than half out put the key 
        map = {}
        n = len(nums)
        for num in nums:
            map[num] = map.get(num, 0) + 1
        for key,value in map.items():
            if value > n // 2:
                return key

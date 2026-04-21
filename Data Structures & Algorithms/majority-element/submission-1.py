class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #create a hashmap and map out frequency 
        #frequencies higher than half out put the key 
        map = {}
        n = len(nums)
        max_number = 0
        tmp = 0
        for num in nums:
            map[num] = map.get(num, 0) + 1
            if max_number < map[num]:
                tmp = num
                max_number = map[num]
        return tmp

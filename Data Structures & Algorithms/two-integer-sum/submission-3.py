class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        answ = []

        for i in range(len(nums)):
            map[nums[i]] = i

            
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in map and map[difference] != i:
                return[i, map[difference]]
        return []
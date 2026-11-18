class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find the bounds
        #use the 

        for i in range(len(nums)):
            if target == nums[i]:
                return i
        return -1
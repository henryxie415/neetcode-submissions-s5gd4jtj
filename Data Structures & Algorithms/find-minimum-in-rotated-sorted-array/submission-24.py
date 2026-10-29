class Solution:
    def findMin(self, nums: List[int]) -> int:
        #establish the bounds once higher number goes to smaller
        #binary search between the bounds 

        l = 0
        r = len(nums) - 1
        res = nums[r]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] < nums[l]:
                r = m - 1
            elif nums[m] >= nums[l]:
                l = m + 1
            #establish the bounds 

        return res 
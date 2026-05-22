class Solution:
    def findMin(self, nums: List[int]) -> int:
        #create the bounds 
        l = 0
        r = len(nums) - 1
        #result is the first number as placeholder
        res = nums[0]
        #while loop to search bounds 
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            #mid point 
            m = (l + r) // 2
            res = min(nums[m], res)
            #if the mid point is smaller than first part then its is in second array
            if nums[m] < nums[l]:
                r = m - 1
            #if midpoint is larger then it is part of the first array
            elif nums[m] >= nums[l]:
                l = m + 1
        return res
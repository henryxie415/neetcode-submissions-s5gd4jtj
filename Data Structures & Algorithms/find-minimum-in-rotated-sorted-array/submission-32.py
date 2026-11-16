class Solution:
    def findMin(self, nums: List[int]) -> int:
        #the idea is to find the lowest number 
        #use binary search 

        #start by establishing the two bounds
        l = 0
        r = len(nums) - 1

        res = nums[0] 

        #establish the while loop 
        while l <= r:

            #if the bounds are already sorted then take the nums[l]
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            #mid point
            m = (l + r) // 2    
            #establish to see if nums[0] or nums[m] is smaller
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1


        return res 


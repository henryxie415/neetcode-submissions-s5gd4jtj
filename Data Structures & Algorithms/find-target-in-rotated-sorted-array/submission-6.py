class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #set the bounds of the binary search 
        l = 0
        r = len(nums) - 1
        #create the while loop
        while l <= r:
            #create the midpoint 
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] >= nums[l]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] < nums[l]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
            #return the midpoint
                else:
                    r = m - 1
        return -1
 

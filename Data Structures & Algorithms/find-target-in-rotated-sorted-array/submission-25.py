class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search to find the pivot (lowest number)
        #the pivot will be used as bound depending if the target is higher or lower than pivot
        #binary search in the correct sorted array
        #return -1 if number is not present 
        l = 0 
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l

        #if the pivot is higher than target the bounds are 
        #l = pivot and r = len(nums) - 1
        #if pivot is lower than taret, the bounds are 
        #l = 0 and r = pivot - 1
        l = 0 
        r = pivot - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        l = pivot
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1 
        #then binary search within bounds 
        


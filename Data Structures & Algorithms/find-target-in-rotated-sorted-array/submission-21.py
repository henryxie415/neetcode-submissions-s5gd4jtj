class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find the bounds
        #first pass to find the pivot
        #the pivot will be used as bound depending if the target is higher or lower than pivot
        #binary search in the correct sorted array
        #return -1 if number is not present 

        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m + 1 
            else:
                r = m
        pivot = l

        l = 0
        r = pivot - 1

        while l <= r:
            m = (l + r)//2
            if nums[m] < target:
                l = m + 1
            elif nums[m] == target:
                return m
            else:
                r = m - 1

        l = pivot
        r = len(nums) - 1

        while l <= r:
            m = (l + r)//2
            if nums[m] < target:
                l = m + 1
            elif nums[m] == target:
                return m
            else:
                r = m - 1
        return -1
        


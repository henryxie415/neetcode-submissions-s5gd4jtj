class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n
        #create a binary search 
        while left < right:
            middle = (left + right - 1) // 2
            if nums[middle] >= target:
                right = middle
            else:
                left = middle + 1
        return left


        #if not then insert into index 
        #if found return the index 

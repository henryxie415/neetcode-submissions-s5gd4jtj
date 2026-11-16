class Solution:
    def findMin(self, nums: List[int]) -> int:
        #the idea is to find the lowest number 
        #use binary search 


        nums = sorted(nums)
        return nums[0]

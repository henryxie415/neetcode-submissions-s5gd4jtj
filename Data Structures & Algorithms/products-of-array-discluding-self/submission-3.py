class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #find the products of the left side except for i 
        #find the products of the right side except for i 
        #multiply them together and append to the final array
        n = len(nums)
        arr = [1] * n
        left = 1
        for i in range(n):
            arr[i] *= left 
            left *= nums[i]

        right = 1
        for i in range(n-1,-1,-1):
            arr[i] *= right
            right *= nums[i]

        return arr
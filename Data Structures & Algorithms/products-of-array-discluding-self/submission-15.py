class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #create an array to hold the results of the products
        n = len(nums)
        res = [1] * n
        prefix = 1
        for i in range(n):
            res[i] = prefix 
            prefix *= nums[i]
        #create the prefix (from left to right) 
        #all products to the left except for self
        postfix = 1
        for i in range(n-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        #multiply with the postfix (right to left) 
        #all products to the right except for self 
        return res
        #return result

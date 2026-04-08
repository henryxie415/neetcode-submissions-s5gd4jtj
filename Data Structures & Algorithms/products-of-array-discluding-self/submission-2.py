class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        #iterate through the list 
        for num in nums:
            #if there is a nonzero number multiply for the final product
            if num:
                prod *= num
            else:
                #count the number of zeros
                zero_cnt += 1
        #if more than 1 zero than the whole array is zero
        if zero_cnt > 1: return [0] * len(nums)

        #create the dynamic array 
        res = [0] * len(nums)

        #loop the nums list
        for i in range(len(nums)):
            #store the initial number
            c = nums[i]
            if zero_cnt > 0:  # there is at least one zero
                #if c is not zero then the product is zero 
                if c != 0:
                    res[i] = 0
                #if c is zero then the prod will be as normal 
                else:
                    res[i] = prod
            else:  
                #if there are no zeros than divide the prod by the current number
                #this will act as getting rid of the current number
                res[i] = prod // c
        #return the list 
        return res
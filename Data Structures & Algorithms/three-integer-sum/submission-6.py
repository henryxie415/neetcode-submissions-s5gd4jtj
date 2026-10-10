class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #output is a list of lists with three numbers 

        #results will be here 
        result = []
        #sorted for organization 
        nums.sort()
        
        #go through the list of nums
        for i in range(len(nums) - 2):
            #if the first number is less than zero then break
            if nums[i] > 0:
                break
            #if duplicate skip to next number and it has gone over the first number already
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            
            

            while l < r:
                total_sum = nums[i] + nums[l] + nums[r]
                if total_sum > 0:
                    r -= 1
                elif total_sum < 0:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return result




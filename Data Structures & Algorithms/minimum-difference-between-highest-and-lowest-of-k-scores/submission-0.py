class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        #sort and then sliding window of k 
        #all that matters is the first and last number
        #the difference is first and last number
        
        nums.sort()
        print(nums)
        current_diff = nums[k - 1] - nums[0]

        res = current_diff
        print(res)
        for i in range(k, len(nums)):
            j = i - k + 1
            update = nums[i] - nums[j]
            j += 1
            res = min(res, update)
        return res



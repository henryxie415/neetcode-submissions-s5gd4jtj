class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        currDiff = nums[k - 1] - nums[0]
        print(currDiff)
        res = currDiff
        
        for i in range(1,len(nums)-1):
            if k < len(nums):
                currDiff = nums[k] - nums[i]
                res = min(res, currDiff)
                k += 1
        return res
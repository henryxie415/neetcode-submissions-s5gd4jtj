class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n 

        while l < r:
            m = (l + (r - 1)) // 2
            if nums[m] > target:
                r = m
            elif nums[m] <= target:
                l = m + 1
        if l and nums[l - 1] == target:
            return l - 1
        else:
            return -1
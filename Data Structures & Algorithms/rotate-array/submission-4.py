class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #use the (i + k) % n
        n = len(nums)
        tmp = [0]*n
        for i in range(len(nums)):
            tmp[(i+k)%n] = nums[i]
        nums[:] = tmp

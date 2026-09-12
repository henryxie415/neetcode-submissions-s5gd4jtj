class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = 0
        res = []
        for left in range(len(nums) - 1):
            right = left + 1
            while right < len(nums):
                if nums[left] + nums[right] == target:
                    res.append(left)
                    res.append(right)
                right += 1
        return res

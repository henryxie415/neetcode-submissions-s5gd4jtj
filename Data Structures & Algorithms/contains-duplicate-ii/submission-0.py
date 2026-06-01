class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        keeper = set()

        for i in range(len(nums)):
            l = i + 1
            while l < len(nums):
                if nums[i] == nums[l] and abs(i - l) <= k:
                    return True
                else:
                    l += 1
        return False
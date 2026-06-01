class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        keeper = set()
        l = 0

        for i in range(len(nums)):

            if i - l > k:
                #add the sum into the set
                keeper.remove(nums[l])
                l += 1
            
            if nums[i] in keeper:
                return True
                
            keeper.add(nums[i])
        return False

        
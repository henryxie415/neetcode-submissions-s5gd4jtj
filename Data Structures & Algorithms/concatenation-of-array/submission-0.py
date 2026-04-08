class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        diff = []
        final = []
        for i in range(len(nums)):
            diff.append(nums[i])
        final = nums + diff
        return final
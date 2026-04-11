class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #pointer to go through the list 
        l = 0
        #second pointer to go through beyond the current pointer 
        #final result output
        r = 1
        while l < len(numbers) - 1:
            for r in range(l,len(numbers)):
                if numbers[l] + numbers[r] == target:
                    return [l+1,r+1]
            l += 1

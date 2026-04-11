class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #pointer to go through the list 
        l = 0
        #second pointer to go through beyond the current pointer 
        #final result output
        arr = []
        r = 1
        while l < len(numbers) - 1:
            for r in range(l,len(numbers)):
                if numbers[l] + numbers[r] == target:
                    arr.append(l + 1)
                    arr.append(r + 1)
                    return arr
            l += 1

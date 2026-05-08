class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #create a binary search function,
        #go through a for loop and look through each list in matrix
        def binary_search(nums: List[int], target: int) -> bool:
            n = len(nums)
            l = 0
            r = n - 1
            while l <= r:
                m = (l + r)// 2
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    return True
            return False 

        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                if binary_search(matrix[i], target):
                    return True

        return False

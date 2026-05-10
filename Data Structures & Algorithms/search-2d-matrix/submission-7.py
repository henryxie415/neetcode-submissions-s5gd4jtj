class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(numbers: List[int], target: int) -> bool:
        #create the binary search 
            n = len(numbers)
            l = 0 
            r = n
            while l < r:
                m = (r + l) // 2
                if numbers[m] < target:
                    l = m + 1
                elif numbers[m] > target:
                    r = m
                else:
                    return True
            return False
        #go through the matrix 
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                res = binary_search(matrix[i], target)
                return res
        return False
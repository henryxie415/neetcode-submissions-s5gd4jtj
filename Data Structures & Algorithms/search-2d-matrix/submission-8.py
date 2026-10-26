class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #find the min in each and the binary search the list 
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == target:
                    return True
        return False
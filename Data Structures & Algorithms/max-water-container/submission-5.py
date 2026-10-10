class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #keep track of the indices for the width 
        #find the min for the height
        #keep track of the total max area 
        l = 0
        r = len(heights) - 1
        total_area = 0
        while l < r:
            max_area = min(heights[l], heights[r]) * (r - l)

            total_area = max(max_area, total_area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return total_area


        
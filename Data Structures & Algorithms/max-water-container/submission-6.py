class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        total_height = 0
        while l < r:
            max_height = min(heights[l], heights[r]) * (r - l)
            total_height = max(max_height, total_height)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return total_height
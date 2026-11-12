class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_volume = 0
        current_volume = 0
        while l < r:
            if heights[l] <= heights[r]:
                current_volume = heights[l] * (r - l)
                l += 1
            else:
                current_volume = heights[r] * (r - l)
                r -= 1                
            max_volume = max(max_volume, current_volume)
        return max_volume
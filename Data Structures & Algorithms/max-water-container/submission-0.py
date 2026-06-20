class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxWater = 0

        while l < r:
            width = r - l
            currWater = min(heights[l], heights[r]) * width

            if currWater > maxWater:
                maxWater = currWater
            
            if(heights[l] > heights[r]):
                r -= 1
            elif (heights[l] <= heights[r]):
                l += 1
            
        return maxWater
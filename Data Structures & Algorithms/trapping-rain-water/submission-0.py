class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        prefix = [-1] * len(height)
        suffix = [-1] * len(height)

        preMax = 0
        for i in range(len(height)):
            if height[i] < preMax:
                prefix[i] = preMax
            elif height[i] > preMax:
                preMax = height[i]

        sufMax = 0
        for i in range(len(height) - 1, 0, -1):
            if height[i] < sufMax:
                suffix[i] = sufMax
            elif height[i] > sufMax:
                sufMax = height[i]
        
        water = 0

        for i in range(len(height)):
            if prefix[i] != -1 and suffix[i] != -1:
                water += min(prefix[i], suffix[i]) - height[i]
        
        return water
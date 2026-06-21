class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            if not stack:
                stack.append(i)
            elif t <= temperatures[stack[-1]]:
                stack.append(i)
            elif t > temperatures[stack[-1]]:
                while stack and t > temperatures[stack[-1]]:
                    j = stack.pop()
                    res[j] = i - j
                stack.append(i)
        
        return res

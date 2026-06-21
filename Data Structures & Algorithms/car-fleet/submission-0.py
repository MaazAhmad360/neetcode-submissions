class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        time_stack = []

        for i in range(len(position)):
            stack.append((position[i], speed[i]))

        stack.sort(reverse=True)

        for car in stack:
            time = (target - car[0]) / car[1]
            if not time_stack:
                time_stack.append(time)
            elif time > time_stack[-1]:
                time_stack.append(time)
            else:
                continue
        
        return len(time_stack)


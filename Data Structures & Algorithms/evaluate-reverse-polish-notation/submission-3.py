class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']

        for c in tokens:
            if c not in ops:
                stack.append(int(c))
            else:
                num1 = stack.pop()
                num2 = stack.pop()

                if c == '+':
                    num = num1 + num2
                    stack.append(num)
                elif c == '-':
                    num = num2 - num1
                    stack.append(num)
                elif c =='*':
                    num = num1 * num2
                    stack.append(int(num))
                elif c == '/':
                    num = num2 / num1
                    stack.append(int(num))
        return int(stack.pop())
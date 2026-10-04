class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == '+':
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(a + b)
            elif c == '-':
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(b - a)
            elif c == '*':
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(a * b)
            elif c == '/':
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(float(b / a))
            else:
                stack.append(c)
        return int(stack[-1])
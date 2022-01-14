class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            stack.append(i)
            if i == "+":
                stack.pop()
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(y+x)
            elif i == "-":
                stack.pop()
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(y-x)
            elif i == "*":
                stack.pop()
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(y*x)
            elif i == "/":
                stack.pop()
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(y/x)
        return int(stack.pop())
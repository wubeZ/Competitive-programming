class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ")":
                stack.append(i)
            else:
                reverse = ""
                while stack[-1] != "(":
                    reverse += stack.pop()
                stack.pop()
                for k in reverse:
                    stack.append(k)
                    
        return "".join(stack)
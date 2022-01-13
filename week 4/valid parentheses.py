class Solution:
    def isValid(self, s: str) -> bool:
        d = {}
        d["("] = ")"
        d["{"] = "}"
        d["["] = "]"
        stack = []
        for i in s:
            if i in d.keys():
                stack.append(i)
            elif len(stack)> 0  and d[stack[-1]] == i:
                    stack.pop()
            else:
                return False
        if len(stack) == 0:
                return True
        else:
            return False
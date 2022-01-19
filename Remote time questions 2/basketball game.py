class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        
        for i in ops:
            if i == "C":
                stack.pop()
            elif i == "D":
                stack.append(int(stack[-1])*2)
            elif i == "+":
                temp1 = int(stack.pop())
                temp2 = temp1 + int(stack[-1])
                stack.append(temp1)
                stack.append(temp2)
            else:
                stack.append(int(i))
                
        return sum(stack)
                    
                
                
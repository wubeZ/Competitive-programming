class MyQueue:

    def __init__(self):
        count = 0
        stack = []
        stack2 = []
        self.stack = stack
        self.stack2 = stack2
    def push(self, x: int) -> None:
        return self.stack.append(x)
                
    def pop(self) -> int:
        print(len(self.stack))
        for i in range(1,len(self.stack)):
            self.stack2.append(self.stack.pop())
        print(self.stack2)
        first = self.stack.pop()
        for j in range(len(self.stack2)):
            self.stack.append(self.stack2.pop())
        return first

    def peek(self) -> int:
        for i in range(1, len(self.stack)):
            self.stack2.append(self.stack.pop())
        first = self.stack.pop()
        self.stack.append(first)
        for j in range(len(self.stack2)):
            self.stack.append(self.stack2.pop())
        return first
    
    def empty(self) -> bool:
        if len(self.stack) == 0: 
            return True 
        else: 
            return False 

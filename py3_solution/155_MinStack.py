class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []  # [[val, min],]
        
        
    def push(self, x: int) -> None:
        minval = self.stack[-1][1] if len(self.stack) > 0 else x
        minval = min(minval, x)
        self.stack.append([x, minval])
        

    def pop(self) -> None:
        del self.stack[-1]
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

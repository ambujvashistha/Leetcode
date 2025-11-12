class MinStack:

    def __init__(self):
        self.arr=[]
        self.minarr=[]
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        if len(self.minarr)==0:
            self.minarr.append(val)
        else:
            self.minarr.append(min(val,self.minarr[-1]))
        

    def pop(self) -> None:
        self.arr.pop()
        self.minarr.pop()

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.minarr[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
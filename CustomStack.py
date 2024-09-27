class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

        pass

    def push(self, x: int) -> None:
        if len(self.stack)<self.maxSize:
            self.stack.append(x)
    
        pass

    def pop(self) -> int:
        if len(self.stack)>0:
            self.stack.pop()
            
        pass
        

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            self.stack[i] += val
        
        
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
    
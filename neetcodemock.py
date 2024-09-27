class IntNode():

    def __init__(self) -> None:
        self.set = set()

    
    def insert(self, value):
        self.set.add(value)
        pass

    def remove(self, value):
        self.set.remove(value)
        pass

    def getRandomValue(self) -> int:
        import random
        print(len(self.set))
        length = len(self.set)
        index = random.randint(0, length)
    
        return self.set

        
    
    def __str__(self) -> str:
        print(self.set)

start = IntNode()

start.insert(5)
start.insert(3)
print(start.getRandomValue())
start.__str__()
from collections import deque

class RecentCounter:

    def __init__(self):
        self.counter = 0 
        self.requests = []
        

    def ping(self, t: int) -> int:
        
        self.requests.append(t)

        range = t-3000

        for time in self.requests:
            if time > range and time<=t:
                self.counter+=1
            elif time<range:
                self.counter-=1
        return self.counter
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
class RecentCounter:

    def __init__(self):
        self.queue = []
        self.l = 0
        

    def ping(self, t: int) -> int:
        self.queue.append(t)
    
        while self.l<(len(self.queue)):
            if self.queue[self.l]>=t-3000:
                return len(self.queue)-self.l
            self.l+=1
        return 1
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
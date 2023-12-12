class OrderedStream:

    def __init__(self, n: int):

        self.n = n
        self.ans = [0]*(self.n)
        self.count = 0

    def insert(self, idKey: int, value: str) -> List[str]:

        self.ans [idKey-1] = value
        left = self.count
        ans = []
        while left < self.n:

            if self.ans[left]!=0:

                ans.append(self.ans[left])
                left+=1

            else:
                break
            
        self.count = left
             
        return ans
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
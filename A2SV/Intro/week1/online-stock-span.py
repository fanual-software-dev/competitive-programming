class StockSpanner:

    def __init__(self):
        self.stack = []
        self.ans = {}
        

    def next(self, price: int) -> int:
        total = 1
        while self.stack and self.stack[-1]<=price:
            total+=self.ans[self.stack[-1]]
            self.stack.pop()
        self.stack.append(price)
        self.ans[price]=total
        return total

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
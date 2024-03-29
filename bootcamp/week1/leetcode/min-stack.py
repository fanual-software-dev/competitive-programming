class MinStack(object):

    def __init__(self):
        self.empty=[]
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.empty.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.empty.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.empty[len(self.empty)-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.empty)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
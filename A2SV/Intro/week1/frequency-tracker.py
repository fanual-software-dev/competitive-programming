class FrequencyTracker:

    def __init__(self):

        self.ans_arr = {}
        self.ans = {}
        

    def add(self, number: int) -> None:
        self.ans[self.ans_arr.get(number,0)] =  self.ans.get(self.ans_arr.get(number,0),0)-1
        self.ans_arr[number] = 1 +self.ans_arr.get(number,0)
        self.ans[self.ans_arr.get(number,0)] = 1 + self.ans.get(self.ans_arr.get(number,0),0) 
        

    def deleteOne(self, number: int) -> None:
        
        if number in self.ans_arr:
            
            self.ans[self.ans_arr.get(number,0)]-=1

            self.ans_arr[number] -=1 
            self.ans[self.ans_arr.get(number,0)] = 1 + self.ans.get(self.ans_arr.get(number,0),0) 
            if self.ans_arr[number] == 0:
                self.ans_arr.pop(number)

    def hasFrequency(self, frequency: int) -> bool:
        
        print(self.ans)

        if self.ans.get(frequency,0)>0 :

            return True
        return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
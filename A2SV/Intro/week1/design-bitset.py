class Bitset:

    def __init__(self, size: int):

        self.size = size

        self.ans_arr = ["0"]*self.size
        self.ans = ["1"]*self.size
        self.dict2 = {"1":self.size,"0":0}
        self.dict1 = {"0":self.size,"1":0}
        

    def fix(self, idx: int) -> None:

        if self.ans_arr[idx] == "0":
            self.dict1["1"]+=1
            self.dict1["0"]-=1
            self.dict2["1"]-=1
            self.dict2["0"]+=1

        self.ans_arr[idx] = "1"
        self.ans[idx] = "0"

        
        

    def unfix(self, idx: int) -> None:

        if self.ans_arr[idx] == "1":
            self.dict1["1"]-=1
            self.dict1["0"]+=1
            self.dict2["1"]+=1
            self.dict2["0"]-=1

        self.ans_arr[idx] = "0"
        self.ans[idx] = "1"
        
        

    def flip(self) -> None:

        u = self.ans_arr
        l = self.dict1

        self.ans_arr = self.ans
        self.dict1 = self.dict2

        self.ans = u
        self.dict2 = l

        
        
        

    def all(self) -> bool:

        return 0 == self.dict1.get("0")
        

    def one(self) -> bool:

        return self.dict1.get("1")!=0 
        

    def count(self) -> int:
        # ans = 0 
        # for n in self.ans_arr:
        #     ans += n == 1 
        return self.dict1["1"]
        

    def toString(self) -> str:
        
        return "".join(self.ans_arr)


        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
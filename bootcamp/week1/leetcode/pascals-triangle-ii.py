class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def check(n,start = [1,1],c = 0):
            if n==0:
                return [1]
            elif n==1:
                return start
            elif c==n-1:
                return start
            new=[]
            for i in range(1,len(start)):
                new.append(start[i]+start[i-1])
            new.insert(0,1)
            new.append(1)
            c+=1
            return check(n,new,c)
        return check(rowIndex)
        
class Solution(object):
    def fizzBuzz(self,n):
        emptylist=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                emptylist.append("FizzBuzz")
            elif i%3==0:
                emptylist.append("Fizz")
            else:
                if i%5==0:
                    emptylist.append("Buzz")
                else:
                    emptylist.append(str(i))
        return emptylist

class Solution(object):
    def romanToInt(self, roman):
        dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        dic2={"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        total=0
        x=0
        y=1
        while len(roman)>1:
            u=roman[x]+roman[y]
            v=roman[x]
            if u in dic2:
                total=total+dic2[u]
                roman=roman[len(u):]
            else:
                total+=dic[v]
                roman=roman[y:]
        else:
            if len(roman)==1:total+=dic[roman]
    
        
        return total
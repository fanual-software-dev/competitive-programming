class Solution:
    def isValid(self, s: str) -> bool:
        dic={"(":")","[":"]","{":"}"}
        lis2=[")","]","}"]
        dic1=[]
        for i in range(len(s)):
            if s[i] in dic:
                dic1.append(s[i])
            elif s[i] in lis2:
                if len(dic1)>0 and dic[dic1[len(dic1)-1]]==s[i]:
                    dic1.pop()
                else:
                    return False
        return len(dic1)==0
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        coll=["0","1","2","3","4","5","6","7","8","9"]
        stack=[]
        coll1=[]
        i=0
        for j in range(len(s)):
            coll1.append(s[j])
        while i<len(coll1):
            if coll1[i]=="[":
                stack.append(i)
                i+=1
            elif coll1[i]=="]":
                st=""
                u=stack.pop()
                j=u-1
                while coll1[j] in coll:
                    st+=coll1[j]
                    j-=1
                st=st[::-1]
                coll1[u+1:i]=coll1[u+1:i]*int(st)
                i=i+len(coll1[u+1:i]*(int(st)-1))+1
            else:
                i+=1
        res=""
        for i in coll1:
            if i not in coll and i!="[" and i!="]":
                res+=i    
        return res
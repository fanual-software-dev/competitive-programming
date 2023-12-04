class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        array=s.split()

        if len(array)==1:
            b=[]
            for i in array[-1]:
                b.append(i)
            return b
        maxl=0
        for i in array:
            maxl=max(maxl,len(i))
        ans=["" for i in range(maxl)]
        for i in range(maxl):
            for j in range(len(array)):
                if i>=len(array[j]):
                    ans[i]+=" "
                else:
                    ans[i]+=array[j][i]
        for i in range(len(ans)):
            for j in range(len(ans[i])-1,-1,-1):
                if ans[i][j]==" ":
                    ans[i]=ans[i][:j]
                else:
                    break
        return ans
class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict1={}
        word="abcdefghijklmnopqrstuvwxyz"
        for i in range(1,27):
            dict1[str(i)]=word[i-1]

        ans=[]
        i=0
        while i <(len(s)):
            if i<len(s)-2 and s[i].isnumeric() and s[i+2]=="#":
                ans.append(dict1[s[i:i+2]])
                i+=3
            else:
                ans.append(dict1[s[i]])
                i+=1
        return "".join(ans)
        
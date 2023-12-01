class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        ans=[]
        n=len(word1)
        m=len(word2)
        for i in range(n):
            if i<m:
                ans.append(word1[i]+word2[i])
            else:
                ans.append(word1[i:])
                break
        if m>n:
            ans.append(word2[i+1:])
            
        return "".join(ans)
        
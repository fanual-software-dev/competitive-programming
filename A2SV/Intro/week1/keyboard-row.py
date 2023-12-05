class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        a = "qwertyuiop"
        b = "asdfghjkl"
        c = "zxcvbnm"
        ans=[]

        for i in words:

            s = 0
            t = 0

            if i[0].lower() in b:
                t=1
            elif i[0].lower() in c:
                t=2
            for j in i:

                u=0

                if j.lower() in b:
                    u=1
                elif j.lower() in c:
                    u=2
                
                if u!=t:
                    s=1
                    break
            if s==0:
                ans.append(i)

        return ans
        
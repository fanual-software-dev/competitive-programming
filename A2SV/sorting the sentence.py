class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        coll=s.split()
        coll1=[0]*len(coll)
        for i in coll:
            j= int(i[-1])
            coll1[j-1] = i[:-1]
        return ' '.join(coll1)

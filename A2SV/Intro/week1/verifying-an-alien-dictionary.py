class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dict1={}

        for i in range(len(order)):
            dict1[order[i]]=i
        
        a=0
        b=0

        for i in range(len(words)):
            
            if a<len(words[i]):
                a=len(words[i])
                b=i
        for i in range(a):
            count=0

            for j in range(1,len(words)):
                if i>=len(words[j]) and j>=b:
                    return False
                elif i<len(words[j]) and i<len(words[j-1]) and dict1[words[j-1][i]]>dict1[words[j][i]]:
                    return False
                elif i<len(words[j]) and i<len(words[j-1]) and dict1[words[j-1][i]]==dict1[words[j][i]]:
                    count+=1
            if count==0:
                return True
        return True
            
       
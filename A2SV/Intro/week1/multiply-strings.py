class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if num1=="0" or num2=="0":
            return "0"
        total1=0
        total2=0
        n1=len(num1)
        n2=len(num2)
        i=0
        while i<len(num1):
            total1+=int(num1[i])*10**(n1-1)
            n1-=1
            i+=1
        i=0
        while i<len(num2):
            total2+=int(num2[i])*10**(n2-1)
            n2-=1
            i+=1
        return str(total1*total2)
        
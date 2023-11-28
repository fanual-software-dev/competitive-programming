class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        
        total=0
        n=len(str(x))
        given=x
        while given:

            d = given % 10
            total+=(d*10**(n-1))
            given=given//10
            n-=1
        return total==x

        
class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        while n>=3:
            r=n%3
            n=n//3
            if r==2:
                return False
        
        return True if n==1 or n==0 else 1==2
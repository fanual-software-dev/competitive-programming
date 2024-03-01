class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def recur(a):
            if a==1:
                return True
            elif a<3:
                return False
            elif a%3!=0:
                return False
            else:
                return recur(a//3)
        return recur(n)
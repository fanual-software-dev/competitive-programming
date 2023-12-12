class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def sum_square(given):
            total=0
            while given>0:
                a=given%10
                given=given//10
                total+=a**2
            return total
        visited=set()
        while n not in visited:
            visited.add(n)
            n=sum_square(n)
            if n==1:
                return True
        return False
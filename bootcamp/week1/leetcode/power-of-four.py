class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def check(n):
            if n==1:
                return True
            elif n<4:
                return False
            else:
                if n%4:
                    return False
                return check(n//4) 
        return check(n)
        
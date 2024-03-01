class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        

        def fun(n,k):

            if n==1:
                return 0
            length = (2**(n-1))//2
            if k==length:
                return n%2
            if k<length:
                return fun(n-1,k)
            return 1-fun(n-1,length if not k%length else k%length)
        return fun(n,k)
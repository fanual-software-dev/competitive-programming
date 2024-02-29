class Solution:
    def fib(self, n: int) -> int:
        prev = 0
        prev_prev = 1
        if n==0:
            return 0
        for i in range(1,n):
            prev,prev_prev = prev_prev,prev+prev_prev
        return prev_prev

1class Solution:
2    def fib(self, n: int) -> int:
3        if n==0 or n==1:
4            return n
5        else:
6            return self.fib(n-1)+ self.fib(n-2)
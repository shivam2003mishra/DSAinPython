1class Solution:
2    def isPowerOfTwo(self, n: int) -> bool:
3        if n<=0:
4            return False
5
6        i=0
7        while 2**i <=n:
8            if 2**i == n:
9                return True
10            i+=1
11        return False
1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        m=len(haystack)
4        n=len(needle)
5
6        for i in range(m-n+1):
7            if(needle == haystack[i : i+n]):
8                return i
9        return -1
10
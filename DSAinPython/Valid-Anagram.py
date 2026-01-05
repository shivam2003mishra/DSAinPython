1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        s.lower()
4        t.lower()
5        a=list(s)
6        b=list(t)
7
8        a.sort()
9        b.sort()
10
11        if a==b:
12            return True
13        return False
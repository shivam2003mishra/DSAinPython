1class Solution:
2    def firstUniqChar(self, s: str) -> int:
3
4        for i in range(len(s)):
5            unique=True
6            for j in range(len(s)):
7                if s[i]==s[j] and i != j:
8                    unique=False
9                    break
10            if unique:
11                return i
12
13        return -1
1class Solution:
2    def reverseOnlyLetters(self, s: str) -> str:
3        s=list(s)
4        left=0
5        right=len(s)-1
6
7        while left <=right:
8            if not s[left].isalpha():
9                left +=1
10            elif not s[right].isalpha():
11                right -=1
12            else:
13                s[left],s[right]=s[right],s[left]
14                left +=1
15                right -=1
16        return "".join(s)
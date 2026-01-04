1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        left=0
4        right=len(s)-1
5
6        while(left < right):
7            while(left < right) and not s[left].isalnum():
8                left +=1
9            while(left < right) and not s[right].isalnum():
10                right -=1
11
12            if s[left].lower() != s[right].lower():
13                return False
14
15            left +=1
16            right -=1
17
18        return True
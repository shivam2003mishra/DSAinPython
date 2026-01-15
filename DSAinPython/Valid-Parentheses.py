1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack=[]
4        pair={'(':')','{':'}','[':']'}
5
6        for c in s:
7            if c in pair:
8                stack.append(c)
9            else:
10                if not stack or pair[stack.pop()] != c:
11                    return False
12
13        return not stack
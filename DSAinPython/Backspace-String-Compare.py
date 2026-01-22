1class Solution:
2    def backspaceCompare(self, s: str, t: str) -> bool:
3        def build(string):
4            stack=[]
5            for x in string:
6                if x=="#":
7                    if stack:
8                        stack.pop()
9                else:
10                    stack.append(x)
11
12            return stack
13
14        return build(s)==build(t)
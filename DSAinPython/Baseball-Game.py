1class Solution:
2    def calPoints(self, operations: List[str]) -> int:
3        stack=[]
4        for op in operations:
5            if op=='C':
6                stack.pop()
7            elif op=='D':
8                stack.append(2*stack[-1])
9            elif op=='+':
10                stack.append(stack[-1]+stack[-2])
11            else:
12                stack.append(int(op))
13
14        return sum(stack)
15
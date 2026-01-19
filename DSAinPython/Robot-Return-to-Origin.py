1class Solution:
2    def judgeCircle(self, moves: str) -> bool:
3        vertical=0
4        horizon=0
5
6        for ch in moves:
7            if ch=='L':
8                horizon -=1
9            elif ch=='R':
10                horizon +=1
11            elif ch=='U':
12                vertical +=1
13            else:
14                vertical -=1
15        if horizon==0 and vertical==0:
16            return True
17        return False
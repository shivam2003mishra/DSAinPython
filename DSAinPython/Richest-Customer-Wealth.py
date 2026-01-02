1class Solution:
2    def maximumWealth(self, accounts: List[List[int]]) -> int:
3        res=[]
4        for i in accounts:
5            a=0
6            for j in i:
7                a +=j
8            res.append(a)
9
10        res.sort()
11
12        return res[-1]
13    
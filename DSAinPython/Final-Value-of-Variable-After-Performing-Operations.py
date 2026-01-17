1class Solution:
2    def finalValueAfterOperations(self, operations: List[str]) -> int:
3        res=0
4        for i in operations:
5            if i== "--X":
6                res -=1
7            elif i=="++X":
8                res +=1
9            elif i=="X--":
10                res -=1
11            else:
12                res +=1
13        return res
14
15        
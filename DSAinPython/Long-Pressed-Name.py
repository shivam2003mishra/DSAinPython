1class Solution:
2    def isLongPressedName(self, name: str, typed: str) -> bool:
3        i=j=0
4
5        while j<len(typed):
6            if i<len(name) and name[i]==typed[j]:
7                i+=1
8            elif j>0 and typed[j]==typed[j-1]:
9                pass
10            else:
11                return False
12            j +=1
13
14        return i == len(name)
15        
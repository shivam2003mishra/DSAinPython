1class Solution:
2    def lengthOfLastWord(self, s: str) -> int:
3        s=s.strip()
4        count=0
5        i=len(s)-1
6        while i>=0 and s[i] != " ":
7            count +=1
8            i-=1
9
10        return count
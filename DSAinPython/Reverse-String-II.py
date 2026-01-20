1class Solution:
2    def reverseStr(self, s: str, k: int) -> str:
3        
4        res=""
5        for i in range(0,len(s),2*k):
6            res +=s[i:i+k][::-1] + s[i+k:i+2*k]
7        return res
8        
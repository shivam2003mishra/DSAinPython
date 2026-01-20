1class Solution:
2    def findTheDifference(self, s: str, t: str) -> str:
3        freq={}
4        for ch in s:
5            freq[ch]=freq.get(ch ,0)+1
6
7        for  ch in t:
8            if ch not in freq or freq[ch]==0:
9                return ch
10            freq[ch] -=1
11
1class Solution:
2    def frequencySort(self, s: str) -> str:
3        count=Counter(s)
4        res=""
5        for ch,n in count.most_common():
6            res +=ch*n
7        return res
8
9
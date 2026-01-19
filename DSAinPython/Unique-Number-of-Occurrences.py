1class Solution:
2    def uniqueOccurrences(self, arr: List[int]) -> bool:
3        freq={}
4        for x in arr:
5            freq[x]=freq.get(x,0)+1
6        count=list(freq.values())
7        count.sort()
8
9        for i in range(1, len(count)):
10            if count[i]==count[i-1]:
11                return False
12
13        return True
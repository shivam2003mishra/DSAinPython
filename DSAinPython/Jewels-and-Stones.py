1class Solution:
2    def numJewelsInStones(self, jewels: str, stones: str) -> int:
3        count=0
4        jewel_set=set(jewels)
5        for ch in stones:
6            if ch in jewel_set:
7                count +=1
8        return count
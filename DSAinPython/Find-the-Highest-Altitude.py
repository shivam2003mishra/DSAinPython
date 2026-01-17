1class Solution:
2    def largestAltitude(self, gain: List[int]) -> int:
3        current=0
4        maxAlt=0
5        for i in gain:
6            current +=i
7            if current > maxAlt:
8                maxAlt=current
9        
10        return maxAlt
11        
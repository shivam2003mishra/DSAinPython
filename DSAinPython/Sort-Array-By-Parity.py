1class Solution:
2    def sortArrayByParity(self, nums: List[int]) -> List[int]:
3        even=[]
4        odd=[]
5
6        for x in nums:
7            if x%2==0:
8                even.append(x)
9            else:
10                odd.append(x)
11
12        return even + odd
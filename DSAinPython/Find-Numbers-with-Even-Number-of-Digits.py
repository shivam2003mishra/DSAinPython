1class Solution:
2    def findNumbers(self, nums: List[int]) -> int:
3        count=0
4        for x in nums:
5            curr=str(x)
6            if len(curr) %2 ==0:
7                count +=1
8        return count
1class Solution:
2    def sortedSquares(self, nums: List[int]) -> List[int]:
3        # newlist=[]
4        # for x in nums:
5        #     curr=x**2
6        #     newlist.append(curr)
7        # newlist.sort()
8        # return newlist
9
10        return sorted(x*x for x in nums)
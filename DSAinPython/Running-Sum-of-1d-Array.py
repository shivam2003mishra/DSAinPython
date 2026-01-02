1class Solution:
2    def runningSum(self, nums: List[int]) -> List[int]:
3        res=0
4        newList=[]
5        for i in nums:
6            res +=i
7            newList.append(res)
8
9        return newList
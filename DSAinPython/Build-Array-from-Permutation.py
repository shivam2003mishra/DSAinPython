1class Solution:
2    def buildArray(self, nums: List[int]) -> List[int]:
3        newList=[]
4        for i in range(len(nums)):
5            newList.append(nums[nums[i]])
6        return newList
7
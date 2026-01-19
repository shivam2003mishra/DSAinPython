1class Solution:
2    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
3        target=[]
4        for i in range(0,len(nums)):
5            target.insert(index[i],nums[i])
6        return target
7        
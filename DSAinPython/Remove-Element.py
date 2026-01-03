1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3         i=0
4         for j in range(len(nums)):
5            if nums[j] != val:
6                 nums[i]=nums[j]
7                 i +=1
8         return i
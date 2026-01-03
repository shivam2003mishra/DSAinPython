1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        if not nums:
4            return 0
5
6        i=0
7        for j in range(1, len(nums)):
8            if nums[j] != nums[i]:
9                i+=1
10                nums[i]=nums[j]
11
12        return i+1
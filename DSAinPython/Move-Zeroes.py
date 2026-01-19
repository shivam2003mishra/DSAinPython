1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        k=0
7        n=len(nums)
8        for i in range(0,n):
9            if nums[i] !=0:
10                temp=nums[k]
11                nums[k]=nums[i]
12                nums[i]=temp
13                k +=1
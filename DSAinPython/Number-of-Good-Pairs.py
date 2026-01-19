1class Solution:
2    def numIdenticalPairs(self, nums: List[int]) -> int:
3        count=0
4        for i in range(0, len(nums)):
5            for j in range(i,len(nums)):
6                if nums[i]==nums[j] and i < j :
7                    count +=1
8        return count
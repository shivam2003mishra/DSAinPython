1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        return len(nums) != len(set(nums))
4
5
6        # for i in range(len(nums)):
7        #     for j in range(i+1,len(nums)):
8        #         if nums[i]==nums[j]:
9        #             return True
10        # return False
11        
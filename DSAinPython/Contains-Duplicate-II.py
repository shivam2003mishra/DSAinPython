1class Solution:
2    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
3        s=set()
4
5        for i in range(len(nums)):
6            if nums[i] in s:
7                return True
8            s.add(nums[i])
9
10            if len(s)>k:
11                s.remove(nums[i-k])
12        return False
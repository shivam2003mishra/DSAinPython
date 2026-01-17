1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        res=0
4        for x in nums:
5            res ^=x
6        return res
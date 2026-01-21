1class Solution:
2    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        nums1=set(nums1)
4        nums2=set(nums2)
5        res=list(nums1 & nums2)
6
7        return res
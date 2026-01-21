1class Solution:
2    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        i=j=0
4        res=[]
5        nums1.sort()
6        nums2.sort()
7
8        while i<len(nums1) and j< len(nums2):
9            if nums1[i]==nums2[j]:
10                res.append(nums1[i])
11                i +=1
12                j +=1
13            elif nums1[i]<nums2[j]:
14                i +=1
15            else:
16                j +=1
17        return res
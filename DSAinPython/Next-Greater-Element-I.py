1class Solution:
2    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        ans=[]
4        
5        for x in nums1:
6            ind=nums2.index(x)
7            greater=-1
8            for i in range(ind+1,len(nums2)):
9                if nums2[i]>x:
10                    greater=nums2[i]
11                    break
12            ans.append(greater)
13        return ans
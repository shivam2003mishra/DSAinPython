1class Solution:
2    def shuffle(self, nums: List[int], n: int) -> List[int]:
3        newList=[]
4        for i in range(n):
5            newList.append(nums[i])
6            newList.append(nums[i+n])
7
8        return newList
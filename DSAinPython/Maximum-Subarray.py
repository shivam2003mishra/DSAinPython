1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        currSum=nums[0]
4        maxSum=nums[0]
5
6        for i in range(1, len(nums)):
7            currSum = max(nums[i] , currSum + nums[i])
8            maxSum= max(currSum, maxSum)
9
10        return maxSum
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        n=len(digits)
4        for i in range(n-1,-1,-1):
5            if(digits[i]<9):
6                digits[i] +=1
7                return digits
8            else:
9                digits[i]=0
10
11        return [1]+digits
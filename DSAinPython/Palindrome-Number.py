1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        res=x
4        curr=0
5
6        while res>0:
7            temp = res%10
8            curr =curr*10 + temp
9            res = res//10
10        
11        if(curr==x):
12            return True
13        return False
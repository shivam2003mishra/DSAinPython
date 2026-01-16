1# The guess API is already defined for you.
2# @param num, your guess
3# @return -1 if num is higher than the picked number
4#          1 if num is lower than the picked number
5#          otherwise return 0
6# def guess(num: int) -> int:
7
8class Solution:
9    def guessNumber(self, n: int) -> int:
10        left=1
11        right=n
12
13        while(left <= right):
14            mid=(left+right)//2
15            res=guess(mid)
16
17            if res==0:
18                return mid
19            elif res==-1:
20                right = mid-1
21            else:
22                left=mid+1
1class Solution:
2    def reverseVowels(self, s: str) -> str:
3        left=0
4        right=len(s)-1
5        vowels=set("aeiouAEIOU")
6        s=list(s)
7        while(left<=right):
8            if s[left] not in vowels:
9                left +=1
10            elif s[right] not in vowels:
11                right -=1
12            else:
13                temp=s[left]
14                s[left]=s[right]
15                s[right]=temp
16
17                left +=1
18                right -=1
19        return "".join(s)
1class Solution:
2    def kidsWithCandies(self, candies, extraCandies):
3        newList=[]
4        max=candies[0]
5        for item in candies:
6            if(max < item):
7                max=item
8
9        for i in candies:
10            if(i+extraCandies >= max):
11                newList.append(True)
12            else:
13                newList.append(False)
14
15        return newList
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        minPrice=float('inf')
4        maxPrice=0
5
6        for price in prices:
7            if price < minPrice:
8                minPrice =price
9            else:
10                maxPrice = max(maxPrice, price- minPrice)
11
12        return maxPrice
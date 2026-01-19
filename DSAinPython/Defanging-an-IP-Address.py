1class Solution:
2    def defangIPaddr(self, address: str) -> str:
3        # return address.replace(".","[.]")
4
5        res=""
6        for x in address:
7            if x=="." :
8                res +="[.]"
9            else:
10                res+=x
11        return res
12        
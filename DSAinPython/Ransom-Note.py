1class Solution:
2    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
3        # return not (Counter(ransomNote) - Counter(magazine))
4        count=Counter(magazine)
5
6        for ch in ransomNote:
7            if count[ch]==0:
8                return False
9            count[ch] -=1
10        return True
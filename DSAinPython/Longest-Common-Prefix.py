1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        for i in range(len(strs[0])):
4            for word in strs[1:]:
5                if i >= len(word) or word[i] != strs[0][i]:
6                    return strs[0][:i]
7
8        return strs[0]
9
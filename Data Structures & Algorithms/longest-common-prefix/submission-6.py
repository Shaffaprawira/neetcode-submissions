class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        
        base = strs[0]

        for i in range(len(base)):
            for s in strs[1:]:
                if (i == len(s) or base[i] != s[i]):
                    return base[0:i]

        return base

       
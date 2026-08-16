from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        """
        while 
        for i in s:
            if i not in t:
                return False
            else:
                continue

        return True
        """

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        
        for i in range(len(s)):
            char1 = s[i]
            char2 = t[i]
            if char1 in d:
                if d[char1] != char2:
                    return False
            else:
                if char2 in d.values():
                    return False
                d[char1] = char2
        
        return True        
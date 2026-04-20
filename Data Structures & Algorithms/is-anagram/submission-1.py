class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m=Counter(s)
        n=Counter(t)
        if m != n:
            return False
        return True
            
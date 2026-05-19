class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        l=Counter(s)
        k=Counter(t)
        return True if l==k else False
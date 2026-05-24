class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        s1counts=Counter(s1)
        s2counts=Counter(s2[:len(s1)])

        if s1counts==s2counts:
            return True

        l=0
        r=len(s1)

        while r<len(s2):
            s2counts[s2[l]]-=1 
            s2counts[s2[r]]+=1 

            if s2counts==s1counts:
                return True
            r+=1
            l+=1
        return False
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""
        # build edgecase first, return minimum substring (which is empty)

        countT,window={},{}

        for c in t:
            countT[c]=1+countT.get(c,0)
            # build the hashmap of count of each character in T
        
        have,need=0,len(countT)
        res,reslen=[-1,-1],float("inf")
        l=0
        # setup default values for the have and need map, left and right indices of of the result, the result length and the left pointer
        for r in range(len(s)):
            c=s[r] #c is the current character//right pointer
            window[c]=1+window.get(c,0) #build the window hashmap of the counts of all the characters in the string
            if c in countT and window[c]==countT[c]:
                # add the have counter if we get a character that we need (must be in the CountTmap)
                have+=1
                #continue moving right until we have==need then enter the while loop
            while have==need:
                #we know we have a possible solution but 
                if (r-l+1)<reslen: #it must be the shortest so far to be updated
                    res=[l,r] # update the left right pointer of the best sol so far
                    reslen=r-l+1 # update the shortest length so far
                window[s[l]]-=1 #whether its the shortest or not, we try to minimize by popping the left
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1 #if by removing a needed character, we remove one from have
                l+=1 #moving left pointer to try and minimize again
        l,r=res
        return s[l:r+1] if reslen != float("inf") else ""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        maxlen=0
        for num in nums:
            if (num-1) not in s:
                l=1
                while num+l in s:
                    l+=1
                maxlen=max(maxlen,l)
        return maxlen

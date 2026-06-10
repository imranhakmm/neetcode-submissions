class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        k=set(nums)
        longest=0
        for num in nums:
            length=0
            while (num+length) in k:
                length+=1
            longest=max(longest,length)
        return longest
            
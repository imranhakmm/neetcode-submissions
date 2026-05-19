class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        k=set(nums)
        longest=0
        for num in k:
            length=1
            while (num+length) in k:
                length+=1
            longest=max(length,longest)
        return longest
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k={}
        for i,num in enumerate(nums):
            complement=target-num
            if complement in k:
                return [k[complement],i]
            k[num]=i

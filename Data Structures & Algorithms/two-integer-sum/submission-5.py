class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in k:
                return [k[diff],i]
            k[num]=i
            
        
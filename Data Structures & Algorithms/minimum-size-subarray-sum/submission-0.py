class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=float('inf')
        for i in range(0,len(nums)):
            cursum=0
            for j in range(i,len(nums)):
                cursum+=nums[j]
                if cursum>=target:
                    res=min(res,j-i+1)
                    break
        return 0 if res==float("inf") else res
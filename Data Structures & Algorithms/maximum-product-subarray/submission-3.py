class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curmin,curmax=1,1
        for n in nums:
            tmp=curmax*n
            curmax=max(curmax*n,curmin*n,n)
            curmin=min(tmp,curmin*n,n)
            res=max(res,curmax)
        return res
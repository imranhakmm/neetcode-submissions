class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        k=set()
        for num in nums:
            if num in k:
                return True
            k.add(num)
        
        return False
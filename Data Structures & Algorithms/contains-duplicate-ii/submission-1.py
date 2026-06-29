class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        element_index = {}
        for i,num in enumerate(nums):
            if num in element_index and abs(element_index[num] - i)<=k:
                return True
            element_index[num]=i
        return False
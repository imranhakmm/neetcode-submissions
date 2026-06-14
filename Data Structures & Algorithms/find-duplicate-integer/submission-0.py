class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        c=Counter(nums)
        print(c)
        for num,count in c.items():
            if count>1:
                return num    
        return 0
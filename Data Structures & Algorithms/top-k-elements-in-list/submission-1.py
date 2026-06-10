class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l=[[] for _ in range(len(nums)+1)]
        count=Counter(nums)
        for num,freq in count.items():
            l[freq].append(num)

        res=[]
        for i in range(len(l)-1,0,-1):
            res.extend(l[i])
            if len(res)==k:
                return res


        
            
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        K=Counter(nums)
        K=dict(sorted(K.items(),key=lambda item:item[1],reverse=True))
        l=[]
        c=0
        for key,elem in enumerate(K):
            l.append(elem)
            c+=1
            if c==k:
                return l


        
            
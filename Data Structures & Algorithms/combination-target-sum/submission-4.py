class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        def dfs(start,remain,path):
            if remain==0:
                res.append(path[:])
                return 
            for i in range(start,len(nums)):
                x=nums[i]
                if x>remain:
                    break
                path.append(x)
                dfs(i,remain-x,path)
                path.pop()
        dfs(0,target,[])
        return res

        
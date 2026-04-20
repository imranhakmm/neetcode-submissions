class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(start: int, remain: int, path: List[int]):
            if remain == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                x = candidates[i]

                if i> start and candidates[i]==candidates[i-1]:
                    continue

                if x > remain:  # pruning because sorted
                    break

                path.append(x)
                dfs(i+1, remain - x, path)  # i (reuse allowed)
                path.pop()

        dfs(0, target, [])
        return res       
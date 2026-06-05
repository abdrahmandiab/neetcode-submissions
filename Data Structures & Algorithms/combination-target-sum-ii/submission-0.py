class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i: int, curList: List[int], total: int):
            if total == target:
                res.append(curList.copy())
                return
            elif total > target or i >= len(candidates):
                return
            
            curList.append(candidates[i])
            dfs(i+1, curList, total + candidates[i])
            curList.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, curList, total)
        dfs(0,[],0)

        return res
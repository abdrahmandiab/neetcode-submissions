class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(index, list_so_far):
            if index == len(nums):
                res.append(list_so_far.copy())
                return
            list_so_far.append(nums[index])
            dfs(index+1, list_so_far)
            list_so_far.pop()
            dfs(index+1, list_so_far)

        dfs(0, [])
        
        return res





# the thinking is, at each step, we consider two branches of the tree:
#   one where 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(remaining: set, taken: list):
            if not remaining:                 # stopping criterion
                res.append([nums[j] for j in taken])
                return
            for j in list(remaining):         # choose which to place next
                dfs(remaining - {j}, taken + [j])
        dfs(set(range(len(nums))), [])
        return res

# The choice:
# At every step, we need to do:
#      Take the element
#      Postpone the element
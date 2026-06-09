class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(index, list_so_far):
            if index == len(nums):
                res.append(list_so_far.copy())
                return
            list_so_far.append(nums[index])
            dfs(index+1, list_so_far)
            list_so_far.pop()
            while index < len(nums)-1 and nums[index] == nums[index+1]:
                index+=1
            dfs(index+1, list_so_far)

        dfs(0, [])
        
        return res
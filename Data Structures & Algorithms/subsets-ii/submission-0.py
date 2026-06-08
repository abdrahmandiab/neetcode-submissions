class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        def backtrack(i, subset):
            if i == len(nums):
                res.add(tuple(subset))
                return
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()
            backtrack(i+1, subset)
        backtrack(0,[])
        return [list(s) for s in res]
        

# a solution maybe to do it in index space first
# Then convert the subset_as_indices to subsets using 
# self.subsets[i] = [nums[j] for j in self.subsets[i]]



# Alternatively, the backtrack
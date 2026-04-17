class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            value_in_dict =  d.get(nums[i],None)
            if not value_in_dict:
                d[nums[i]] = i
            else:
                if nums[i]*2 == target:
                    return [value_in_dict,i]

        for i in range(len(nums)):
            complement = target - nums[i]
            idx_c = d.get(complement, None)
            if idx_c and idx_c != i:
                return [i,idx_c] if i < idx_c else [idx_c, i]
        
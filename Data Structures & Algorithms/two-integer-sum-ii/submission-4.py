class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        lp = 0
        rp = n-1
        while lp < rp:
            t = numbers[lp] + numbers[rp]
            if t == target:
                return [lp+1, rp+1]
            elif t> target:
                rp-=1
            else:
                lp+=1
        return []

        
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(0)
            num = i
            while num:
                num &= num-1 # (remove lowest set 1)
                res[i]+=1
        return res
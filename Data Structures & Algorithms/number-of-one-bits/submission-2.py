class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            print(bin(n))
            n &= n-1
            res +=1
        return res
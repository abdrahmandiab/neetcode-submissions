class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            print(bin(n), bin(n-1))
            n &= n-1
            res +=1
        return res
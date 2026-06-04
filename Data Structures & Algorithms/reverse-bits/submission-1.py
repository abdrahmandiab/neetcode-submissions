class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:]
        n = n[::-1]
        j = "0" * (32-len(n))
        print(n,)
        return int(n+j,2)
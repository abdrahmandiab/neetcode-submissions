class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        for _ in range(n):
            res*= x
        for _ in range((-1*n)):
            res/=x
        return res
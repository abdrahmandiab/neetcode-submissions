class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            digit_sum = sum([int(c)**2 for c in str(n)])
            if digit_sum ==1:
                return True
            if digit_sum in seen:
                return False
            seen.add(digit_sum)
            n = digit_sum
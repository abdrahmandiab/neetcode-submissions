class Solution:
    def reverse(self, x: int) -> int:
        neg_mask = 0xFFFFFFFF
        s = str(x)
        num_chars = len(s)
        res =0 
        was_neg = False
        end = -1
        if x < 0:
            was_neg = True
            end = 0
            x = x*-1
        for r in range(num_chars-1,end,-1):
            curr_digit = x%10
            x = x // 10
            res = (res*10) + curr_digit
        if res > pow(2,31):
            return 0
        if was_neg:
            res *= -1
        return res

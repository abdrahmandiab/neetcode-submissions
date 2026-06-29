class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        two_right = 1          # empty tail
        one_right = 1          # last char is non-'0' (guarded above for s[0], but
                            # actually set this by processing properly):
        for i in range(len(s) - 1, -1, -1):
            cur = 0
            if s[i] != '0':
                cur += one_right
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                cur += two_right
            two_right = one_right
            one_right = cur
        return one_right


# How can we use DP here
# save the result of possible combinations up to index in
# 120210
#  the example above^ can only be construed as:
#. > (1) (20) (2) (10)
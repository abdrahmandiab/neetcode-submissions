class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            target_char = s[r]
            count[target_char] +=1
            maxf = max(maxf, count[target_char])
            while (r-l-maxf+1) > k: #(l>XYY<rX)
                count[s[l]] -= 1
                l+=1
            res = max(res, r-l+1)
        return res
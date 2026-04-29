class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_idx_of_map = {}
        # { #for ->abcbc
        # a: 0
        # b: 1 
        # c: 2
        #}
        l = 0
        ret = 0
        for idx in range(len(s)):
            if s[idx] in last_idx_of_map:
                l = max(last_idx_of_map[s[idx]]+1, l )
            last_idx_of_map[s[idx]] = idx
            ret = max(ret, idx-l + 1)
            
        return ret
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        for c in t:
            if d[c] == 0:
                return False
            d[c] -= 1
        for key, value in d.items():
            if value != 0:
                return False
        return True
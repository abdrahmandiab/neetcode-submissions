class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            counts = [0]*26
            for c in s:
                counts[ord(c)-ord('a')] += 1
            d[tuple(counts)].append(s)
        return list(d.values())
            
                
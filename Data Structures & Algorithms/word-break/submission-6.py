class Trie:
    def __init__(self):
        self.trie = {}
    def insert(self, word: str):
        d = self.trie
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d['.'] = "."
    def search(self, word: str):
        d = self.trie
        for c in word:
            if c not in d:
                return False
            d = d[c]
        return '.' in d


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        t = 0 # upper bound for maximum word length
        for word in wordDict:
            trie.insert(word)
            t = max(t, len(word))
        
        n = len(s)
        dp = [False]*(n+1)
        dp[n] = True
        for i in range(n,-1,-1):
            for j in range(i+1, min(n+1, i + t +1)):
                if trie.search(s[i:j]):
                    
                    dp[i] = dp[j]
                    if dp[i]:
                        break
        return dp[0]

# s = "neetcode"
# at s[4:5], s[4:6], s[4:7] -> skip
# at s[4:8] -> dp[4] = dp[8], d[8] is True. so dp[4] is True now

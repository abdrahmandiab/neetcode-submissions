class Trie:
    def __init__(self):
        self.trie = {}
    
    def insert(self, word):
        d = self.trie
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d["$"] = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for w in words:
            root.insert(w)
        
        NROWS, NCOLS = len(board), len(board[0])
        res = set()
        visit = set()
        def dfs(r,c,node,word):
            if (r <0 or c< 0 or r==NROWS or c==NCOLS
            or (r,c) in visit or board[r][c] not in node):
                return
            visit.add((r,c))
            node = node[board[r][c]]
            word += board[r][c]
            if node.get("$", False):
                res.add(word)
            dfs(r-1,c, node, word)
            dfs(r+1,c, node, word)
            dfs(r,c-1, node, word)
            dfs(r,c+1, node, word)
            visit.remove((r,c))
        for r in range(NROWS):
            for c in range(NCOLS):
                dfs(r,c,root.trie,"")
        return list(res)
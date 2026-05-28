class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        d = self.trie
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d["$"] = True

    def search(self, word: str) -> bool:
        return self.searchHelper(word,self.trie)
        
    def searchHelper(self, word, d) -> bool:
        for i, c in enumerate(word):
            if c == ".":
                for k, v in d.items():
                    if k == "$":
                        continue
                    if self.searchHelper(word[i+1:],v):
                        return True
                return False
            elif c not in d:
                return False
            else: # c in d
                d = d[c]
        return "$" in d
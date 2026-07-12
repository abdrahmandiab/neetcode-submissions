class DSU:
    def __init__(self, n):
        self.comps = n
        self.parent = list(range(n+1))
        self.size = [1]*(n+1)
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False

        self.comps -= 1

        if self.size[pu] >= self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv
        return True
    
    def components(self):
        return self.comps



class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)>n-1:
            return False
        dsu = DSU(n)
 
        for fromm,to in edges:
            if not dsu.union(fromm, to):
                return False
        return dsu.components()==1





















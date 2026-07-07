class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n==0:
            return True
        visit = set()
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(i: int = 0, prev: int = -1):
            if i in visit:
                return False
            visit.add(i)
            for node in adj[i]:
                if node == prev:
                    continue
                if not dfs(node,i):
                    return False
            return True
        return dfs() and n==len(visit)

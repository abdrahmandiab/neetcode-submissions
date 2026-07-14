class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}
        tickets.sort()
        for from_i, to_i in tickets:
            adj[from_i].append(to_i)
        
        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets)+1: # already visited all destinations
                return True # finish with True
            if src not in adj: # src not in Adj -> scrap this path, return False
                return False
            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v): return True
                # if above is True, we return^^
                adj[src].insert(i,v) # insert v at position i in the list
                res.pop()
            return False
        dfs("JFK")
        return res
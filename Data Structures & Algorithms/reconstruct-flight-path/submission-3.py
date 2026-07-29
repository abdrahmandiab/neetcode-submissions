class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        # adj = {}
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)
        # adj = {   'JFK' : ['BUF']
        #           'BUF' : ['HOU']
        #           'HOU' : ['SEA']}
        res = []
        def dfs(src): # 'JFK'
            while adj[src]: #['BUF']
                dst = adj[src].pop() #'BUF'
                dfs(dst) # dfs('BUF') # .. # dfs('SEA')
            res.append(src) # res = ['SEA'], res = ['SEA', 'HOU'], res = ['SEA', 'HOU', 'BUF'], res = ['SEA', 'HOU', 'BUF', 'JFK']
        
        dfs('JFK')
        return res[::-1] # ['JFK','BUF', 'HOU', 'SEA']
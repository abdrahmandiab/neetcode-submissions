class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
        def dfs(i, r, c):
            if i == len(word):
                return True
            if r<0 or c<0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or visited[r][c]:
                return False

            visited[r][c] = True
            res = (dfs(i+1,r+1,c) or
                    dfs(i+1,r-1,c) or 
                    dfs(i+1,r,c+1) or
                    dfs(i+1,r,c-1))
            visited[r][c] = False
            return res
            
            
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0,r,c):
                    return True
        return False



# This is a DP problem normally, since we just need to find one instance
# Backtrack is good when we need to find all instances.
# in this case, we would find ALL words. (and break when word == target word)

# the pesky thing is enforcing the condition of not visiting same cell more than once
# to resolve this, I will use a set() called visited and check before I add a letter if
# its coordinate is in visited.


# How does the tree look like, we have m * n trees in total
# it starts with one letter, let's take the first A at 0,0
#.                A
#.             /     \
#             AB     AS
# Realistically this wouldn't play in the first place, we cut it at the top a
# Let's now take C at 0,2
#                    c
#              ca    cb(cut)  cd(cut)
#         caa caa cat
# So at each step :
# 1. Check if current == word -> if yes, break
# 2. if not, we have to take one of four directions as the next combination.
# 3. 
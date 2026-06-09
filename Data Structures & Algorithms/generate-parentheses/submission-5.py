class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.acc = ""
        def backtrack(o, c):
            if o + c == 2*n and o == c == n:
                res.append(self.acc)
                return
            if o < n:                
                self.acc+="("
                backtrack(o+1,c)
                self.acc = self.acc[0:-1]
            if c < o:
                self.acc+=")"
                backtrack(o, c+1)
                self.acc = self.acc[0:-1]
        backtrack(0,0)
        return res



# For each new bracket pair
# There are 3 options, either it goes at the start, around the existing portion, or at the end.
# This leads to a lot of duplicates
# can handle using sets

# there is probably an easier way.
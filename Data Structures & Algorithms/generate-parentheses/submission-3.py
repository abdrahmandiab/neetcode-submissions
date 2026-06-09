class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtrack(opened, closed):
            if opened == closed == n:
                res.append("".join(stack))
                return
            if opened < n:
                stack.append("(")
                backtrack(opened +1, closed)
                stack.pop()
            if closed < opened:
                stack.append(")")
                backtrack(opened, closed+1)
                stack.pop()
        backtrack(0,0)
        return res



# For each new bracket pair
# There are 2 options, either it goes at the end
# 
class Solution:
    def checkValidString(self, s: str) -> bool:
        lb, rb = 0,0
        for c in s:
            if c == "(":
                lb+=1
                rb+=1
            if c == ")":
                lb-=1
                rb-=1
            if c == "*":
                if lb>0:
                    lb-=1
                rb+=1
            if rb <0:
                return False
            if lb < 0:
                lb = 0

        return lb == 0

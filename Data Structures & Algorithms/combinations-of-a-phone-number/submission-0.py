class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combi = {
            "2":"abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        ret = []
        if len(digits)==0:
            return ret
        def backtrack(i:int, cur: str):
            if i == len(digits):
                ret.append(cur)
                return
            for char in combi[digits[i]]:
                backtrack(i+1, cur+char)
        backtrack(0, "")
        return ret
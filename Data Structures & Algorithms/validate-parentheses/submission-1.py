class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = ["[", "{", "("]
        closes = []
        for char in s:
            if char in opens:
                stack.append(char)
            else:
                if stack:
                    top = stack.pop()
                    if char == "]":
                        if  top != "[":
                            return False
                    elif char == "}":
                        if  top != "{":
                            return False
                    elif char == ")":
                        if  top != "(":
                            return False
                    else:
                        pass
                else:
                    return False

        return (stack == [])
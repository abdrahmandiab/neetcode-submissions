class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for char in tokens:
            if char in "+-*/":
                op1 = operands.pop()
                op2 = operands.pop()
                if char == "+":
                    operands.append(op1+op2)
                if char == "*":
                    operands.append(op1*op2)
                if char == "-":
                    operands.append(op2-op1)
                if char == "/":
                    operands.append(int(op2/op1))
            else:
                operands.append(int(char))
        return operands[-1]
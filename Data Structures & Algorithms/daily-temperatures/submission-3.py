class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0]*len(temperatures)
        stack = [] # store days that haven't found a warmer day
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                ret[stackInd] = i - stackInd
            stack.append((t,i))

        return ret
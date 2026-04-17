class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        nh = len(heights)
        max_total = 0
        L_stack = []
        R_stack = []
        LB = [-1]*nh
        RB = [-1]*nh

        for i,h in enumerate(heights):
            new = (h,i)
            while R_stack and h < R_stack[-1][0]:
                RB[R_stack[-1][1]] = i
                R_stack.pop()
            R_stack.append(new)

            while L_stack and h <= L_stack [-1][0]:
                L_stack.pop()
            LB[i] = L_stack[-1][1] if L_stack else -1
            L_stack.append(new)
                
        for h,i in R_stack:
            RB[i] = nh
        
        print(RB, LB)

        for h, r ,l in zip(heights,RB, LB):
            area = h * (r-l-1)
            print(area)
            max_total = max(area, max_total)

        return max_total
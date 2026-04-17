class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and h <= stack[-1][1]:
                index, height = stack.pop()
                maxArea = max(maxArea, height*(i-index))
                start = index
            stack.append((start,h))
        
        # Go over the stack remnants, stretch them out to the very end on the right side
        for i, h in stack:
            maxArea = max(maxArea, h* (len(heights)-i))

        return maxArea





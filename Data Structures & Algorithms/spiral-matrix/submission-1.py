class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        order = []
        top, bottom = 0, len(matrix)
        left,right = 0, len(matrix[0])
        while bottom > top and right > left :
            # first take along top row [left to right]
            for i in range(left,right,1): 
                order.append(matrix[top][i])
            top +=1
            # then take along column at right side [top to bot]
            for j in range(top,bottom):
                order.append(matrix[j][right-1])
            right-=1
            if not (left < right and top < bottom):
                break
            # then take along row reversed at bottom
            for i in range(right-1,left-1, -1):
                order.append(matrix[bottom-1][i])
            bottom-=1
            # then take along column reversed at the left side
            for j in range(bottom-1, top-1, -1):
                order.append(matrix[j][left])
            left+=1
        return order

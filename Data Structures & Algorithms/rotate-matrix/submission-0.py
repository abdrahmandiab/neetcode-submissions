class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        # dissect layer by layer
        # to take the outter layer, we want (l = 0, r = n-1) and this goes for both L->R AND bot-top
        while l < r:
            for i in range(r-l): # not l -> r-l? 
                top, bottom = l, r  # say 0, 1

                topLeft = matrix[top][l+i] # matrix[0][0]

                matrix[top][l+i] = matrix[bottom - i][l] # matrix[0][0] = matrix[1-0][0]

                matrix[bottom-i][l] = matrix[bottom][r-i] # matrix[1][0] = matrix[1][1]

                # matrix[1][1] = matrix[0][1]
                matrix[bottom][r-i] = matrix[top+i][r]

                matrix[top+i][r] = topLeft


            r-=1
            l+=1
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lm,rm = 0, len(matrix)-1
        while lm <=rm:
            mid = lm + ((rm - lm) //2)
            if matrix[mid][0] > target: # go lower
                rm = mid -1
            elif matrix[mid][-1] < target:
                lm = mid + 1
            else:
                l, r = 0, len(matrix[mid])-1
                while l<=r:
                    m = l + ((r-l)//2)
                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] > target:
                        r = m-1
                    else:
                        l = m+1
                return False
        return False

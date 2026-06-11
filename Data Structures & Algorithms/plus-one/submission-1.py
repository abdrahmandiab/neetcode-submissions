class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        ptr = -1
        while ptr > (-1*n) -1 and digits[ptr] == 9 :
            digits[ptr] = 0
            ptr -= 1
        if ptr < (-1*n):
            return [1] + digits
        digits[ptr]+=1

        return digits
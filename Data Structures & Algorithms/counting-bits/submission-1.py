class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            num_ones = 0
            while i:
                if i & 1:
                    num_ones+=1
                i >>= 1
                
            res.append(num_ones)
        return res